import http.cookiejar
import json
import os
import re
import secrets
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

from app.auth import hash_password

IMAGE = sys.argv[1] if len(sys.argv) > 1 else "dfe-copilot:ci"
ROOT = Path(__file__).resolve().parents[1]
REPORT = Path(os.environ.get("FISC_SMOKE_REPORT", "/tmp/fisc-smoke-runtime.json"))


def docker(*args, data=None):
    return subprocess.check_output(["docker", *args], input=data, text=True).strip()


password = secrets.token_urlsafe(24)
env = {
    name: secrets.token_urlsafe(32)
    for name in ["API_KEY", "A2A_API_KEY", "EVENT_MESH_API_KEY", "ADMIN_API_KEY", "SESSION_SECRET"]
}
env.update(
    {
        "WEB_UI_USERS": "validation:" + hash_password(password),
        "REQUIRE_AUTH": "true",
        "DATABASE_URL": "",
        "REDIS_URL": "",
        "GRAPH_RAG_ENABLED": "false",
        "CHECKPOINTING_ENABLED": "false",
        "AMQP_ENABLED": "false",
        "WEB_SEARCH_ENABLED": "false",
        "DFE_KB_ENABLED": "false",
        "QDRANT_URL": "http://127.0.0.1:9",
        "OLLAMA_HOST": "http://127.0.0.1:9",
    }
)
jar = http.cookiejar.CookieJar()
client = urllib.request.build_opener(
    urllib.request.ProxyHandler({}), urllib.request.HTTPCookieProcessor(jar)
)
container = None
with tempfile.TemporaryDirectory(prefix="fisc-runtime-") as tmp:
    file = Path(tmp) / "runtime.env"
    file.write_text("\n".join(f"{k}={v}" for k, v in env.items()) + "\n")
    file.chmod(0o600)
    try:
        container = docker(
            "run",
            "--rm",
            "--detach",
            "--env-file",
            str(file),
            "--publish",
            "127.0.0.1::8000",
            IMAGE,
        )
        port = docker("port", container, "8000/tcp").rsplit(":", 1)[1]
        base = "http://127.0.0.1:" + port

        def request(path, body=None):
            data = json.dumps(body).encode() if body is not None else None
            return client.open(
                urllib.request.Request(
                    base + path, data=data, headers={"Content-Type": "application/json"}
                ),
                timeout=5,
            )

        deadline = time.monotonic() + 90
        while True:
            try:
                with request("/health") as response:
                    assert json.load(response) == {"status": "ok"}
                break
            except (OSError, urllib.error.URLError):
                if time.monotonic() > deadline:
                    raise
                time.sleep(0.5)
        try:
            request("/domain-plugins")
            raise AssertionError("Unauthenticated catalog accepted")
        except urllib.error.HTTPError as error:
            assert error.code == 401
        with request("/auth/login", {"username": "validation", "password": password}) as response:
            assert json.load(response)["authenticated"]
            assert response.headers["Set-Cookie"].startswith("dfe_session=")
            assert "HttpOnly" in response.headers["Set-Cookie"]
        with request("/domain-plugins") as response:
            catalog = json.load(response)
            assert [p["name"] for p in catalog["plugins"]] == ["dfe"]
        with request("/") as response:
            html = response.read().decode()
            assert "FISC" in html
        assets = re.findall(r'(?:src|href)="([^"]+\.(?:js|css))"', html)
        assert assets
        for asset in assets:
            with request(asset) as response:
                assert response.status == 200
        try:
            request(
                "/diagnose",
                {
                    "description": "Contexto sintético inválido",
                    "domain_context": {"environment": "invalid"},
                },
            )
            raise AssertionError("Invalid fiscal context accepted")
        except urllib.error.HTTPError as error:
            assert error.code == 422
        code = """
import importlib.util,os,pathlib,sys,json
from importlib.metadata import version
from dfe_copilot.resources import DATA_DIR,UI_DIR
from dfe_copilot.fiscal.xml_tools import SchemaPackage,analyze_fiscal_xml
from dfe_copilot.plugin import PLUGIN
assert os.getuid()!=0
assert importlib.util.find_spec('iic_copilot') is None
assert not pathlib.Path('/runtime/src').exists()
assert not pathlib.Path('/runtime/packages').exists()
assert 'site-packages' in str(DATA_DIR) and 'site-packages' in str(UI_DIR)
assert (UI_DIR/'index.html').is_file()
assert '+cpu' in version('torch')
result=analyze_fiscal_xml(sys.stdin.read().encode(),SchemaPackage.load())
assert result['xsd_validation']=='valid',result
key='35261111222333000181550010000000011000000014'
payload='<protNFe xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00"><infProt><tpAmb>2</tpAmb><verAplic>DEMO</verAplic><chNFe>'+key+'</chNFe><dhRecbto>2026-11-11T09:52:00-03:00</dhRecbto><cStat>204</cStat><xMotivo>Rejeicao: Duplicidade de NF-e</xMotivo></infProt></protNFe>'
events=[{'evidence_id':name,'document_ref':key,'at':at,'event':event} for name,at,event in [('A','2026-11-11T12:59:00Z','sent'),('T','2026-11-11T13:00:00Z','timeout'),('B','2026-11-11T13:00:01Z','sent')]]
findings=PLUGIN.run({'payload':payload,'domain_context':PLUGIN.validate_context({'environment':'homologation','jurisdiction':'SP','events':events})})
assert {'F-cStat','F-204','H1'}<={f['id'] for f in findings},findings
from proton import SSL
assert SSL.present()
print(json.dumps({'python':sys.version.split()[0],'torch':version('torch'),'core':version('copilot-core'),'fisc':version('dfe-copilot'),'non_root':True,'xsd':'valid','fiscal_findings':[f['id'] for f in findings],'no_iic_source':True,'amqp_tls':True}))
"""
        resources = json.loads(
            docker(
                "exec",
                "-i",
                container,
                "python",
                "-c",
                code,
                data=(ROOT / "tests/fixtures/nfe_controle_positivo_sp.xml").read_text(),
            )
        )
        with request("/auth/logout", {}) as response:
            assert json.load(response)["ok"]
        with request("/auth/session") as response:
            assert not json.load(response)["authenticated"]
        REPORT.write_text(
            json.dumps(
                {
                    "image": IMAGE,
                    "image_id": docker("image", "inspect", IMAGE, "--format", "{{.Id}}"),
                    "http": {
                        "health": True,
                        "unauthenticated_401": True,
                        "login": True,
                        "cookie_http_only": True,
                        "fiscal_catalog": True,
                        "ui_assets": True,
                        "invalid_context_422": True,
                        "logout": True,
                    },
                    "resources": resources,
                    "limitations": [
                        "no live LLM inference",
                        "no real SAP or SEFAZ",
                        "no remote Qdrant or PostgreSQL",
                    ],
                },
                indent=2,
            )
            + "\n"
        )
        print(REPORT.read_text())
    finally:
        if container:
            subprocess.run(
                ["docker", "rm", "--force", container],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False,
            )
