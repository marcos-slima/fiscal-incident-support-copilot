# FISC — execução independente

O código está na raiz deste repositório. As bibliotecas são obtidas de releases
públicas de [Copilot Platform](https://github.com/marcos-slima/copilot-platform)
por versão e hash; checkout do IIC ou da plataforma não é necessário.

## Ambiente de desenvolvimento

Requisitos: Python 3.12+, uv 0.13.4, Node.js 22+, cmake, make, gcc,
pkg-config, libssl-dev, libffi-dev e libsasl2-dev no Linux.

~~~bash
uv sync --locked --python 3.12 --no-install-project
npm ci --prefix frontend --ignore-scripts
npm run build --prefix frontend
DFE_BUILD_REQUIRE_UI=1 uv build --wheel --no-sources --out-dir dist
uv pip install --python .venv/bin/python --no-deps dist/dfe_copilot-0.1.0-py3-none-any.whl
uv run --no-sync python -I scripts/verify_install.py
uv run --no-sync python -I -m pytest -c pyproject.toml -o pythonpath= tests -q
~~~

--no-deps no passo de instalação do produto pressupõe que o primeiro comando
já instalou as dependências do lock. Não é atalho para uma instalação sem dependências.

Na execução nativa, configure WEB_UI_USERS, SESSION_SECRET, API_KEY,
OLLAMA_HOST e QDRANT_URL conforme o ambiente e então use:
uv run --no-sync uvicorn dfe_copilot.main:app --port 8001.
As variáveis DFE_* do exemplo abaixo são mapeadas pelo Compose, não pela
execução nativa.

## Docker e primeiro acesso

O Dockerfile compila a UI e o wheel fiscal e instala apenas os wheels na imagem
final. Modelos não são incorporados: provisione Ollama e embeddings no host.

1. Copie .env.example para .env.
2. Gere o hash da senha sem registrá-la no histórico:
   uv run --no-sync python -c 'from getpass import getpass; from app.auth import hash_password; print(hash_password(getpass()))'
3. Configure DFE_WEB_UI_USERS com usuario:hash e DFE_SESSION_SECRET com segredo
   estável. Configure as chaves de API e os modelos do deployment, sem versioná-los.
4. Execute docker compose --env-file .env up -d --build.
5. Abra http://127.0.0.1:8002; a porta é publicada apenas em loopback.

O Compose cria rede e Qdrant próprios; não migra dados nem usa credenciais do
IIC. A base fiscal começa vazia. Com modelos provisionados, a ingestão explícita
é docker compose exec dfe python -m dfe_copilot.kb ingest.
O MOC opcional deve ser provisionado conforme data/corpus/manifest.json;
não é distribuído nem baixado automaticamente pelo build.

## Serviços existentes e revisão persistente

compose.existing.yaml preserva os mounts read-only de caches e exige rede,
Qdrant URL e modelo de embedding explícitos. Não executa ingestão/reset.

Para revisão persistente, configure DFE_POSTGRES_PASSWORD e
DFE_LLM_CREDENTIALS_MASTER_KEY (chave Fernet) e use em conjunto
-f compose.yaml -f compose.review.yaml. O pacote operacional está na imagem em
/opt/copilot-operations. Aplicar as migrations do core no banco do deployment
é uma ação explícita anterior ao uso persistente:

~~~bash
docker compose --env-file .env -f compose.yaml -f compose.review.yaml up -d postgres qdrant
docker compose --env-file .env -f compose.yaml -f compose.review.yaml run --rm dfe alembic -c /opt/copilot-operations/alembic.ini upgrade head
docker compose --env-file .env -f compose.yaml -f compose.review.yaml up -d dfe
~~~

Backup, verificação do banco de destino e compatibilidade de dados pertencem
à operação do deployment. Este guia não comprova execução em PostgreSQL real
na extração. Confira os limites em VALIDACAO_FORA_MONOREPO.md.

## Verificação da imagem

~~~bash
docker build -t dfe-copilot:ci .
uv run --no-sync python -I scripts/smoke_image.py dfe-copilot:ci
~~~

O smoke usa credenciais efêmeras e XML sintético, remove o contêiner temporário
e não faz inferência LLM real, consulta SAP/SEFAZ ou escrita fiscal.
