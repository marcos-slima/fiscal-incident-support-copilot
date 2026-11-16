FROM node:22-slim AS frontend
WORKDIR /ui
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci --ignore-scripts
COPY frontend/ ./
RUN npm run build

FROM ghcr.io/astral-sh/uv:0.13.4 AS uv
FROM python:3.12-slim AS builder
COPY --from=uv /uv /usr/local/bin/uv
RUN apt-get update && apt-get install -y --no-install-recommends cmake make gcc libssl-dev libffi-dev libsasl2-dev pkg-config && rm -rf /var/lib/apt/lists/*
ENV UV_LINK_MODE=copy UV_PYTHON_DOWNLOADS=never
WORKDIR /runtime
COPY pyproject.toml uv.lock LICENSE README.md ./
RUN uv sync --locked --no-dev --no-install-project
COPY src/ src/
COPY data/ data/
COPY hatch_build.py ./
COPY --from=frontend /ui/dist frontend/dist
RUN DFE_BUILD_REQUIRE_UI=1 uv build --wheel --no-sources --out-dir /wheels \
    && uv pip install --python .venv/bin/python --no-deps /wheels/dfe_copilot-*.whl \
    && .venv/bin/python -c "from proton import SSL; assert SSL.present()"
COPY shared-libraries.json ./
COPY scripts/fetch_operations.py scripts/fetch_operations.py
RUN .venv/bin/python scripts/fetch_operations.py /opt/copilot-operations

FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends libsasl2-2 && rm -rf /var/lib/apt/lists/* && useradd --create-home --uid 1000 fisc
WORKDIR /runtime
COPY --from=builder --chown=fisc:fisc /runtime/.venv /runtime/.venv
COPY --from=builder --chown=fisc:fisc /opt/copilot-operations /opt/copilot-operations
ENV PATH=/runtime/.venv/bin:$PATH PYTHONUNBUFFERED=1 HF_HUB_DISABLE_TELEMETRY=1
USER fisc
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=15s CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=3)"
CMD ["/runtime/.venv/bin/uvicorn", "dfe_copilot.main:app", "--host", "0.0.0.0", "--port", "8000"]
