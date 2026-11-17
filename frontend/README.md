# UI do FISC — @copilot/dfe-ui

Interface fiscal independente, consumindo @copilot/core-ui por tarball versionado.
O formulário deriva do schema de FiscalContext publicado pelo plugin dfe em
GET /domain-plugins. Não importa componentes do IIC; não oferece escrita fiscal.

Na raiz deste repositório:

~~~bash
npm ci --prefix frontend --ignore-scripts
npm run dev --prefix frontend
npm run lint --prefix frontend
npm run typecheck --prefix frontend
npm run build --prefix frontend
~~~

Vite usa 5174 e encaminha a API para 127.0.0.1:8001; DFE_API_URL sobrescreve o
destino. O build gera frontend/dist, incluído no wheel em dfe_copilot/_ui.
A execução Python deve seguir [o guia instalado](../docs/DEPLOY.md), com
uvicorn dfe_copilot.main:app. Não usar uv --all-packages nem os workspaces npm
do antigo monorepo. Para servir um build local pela API, configure UI_DIST_DIR=frontend/dist.
O deployment Compose padrão publica a API em 8002; a porta nativa é configurável.

O login usa usuários do deployment e cookie dfe_session; ativar conta não cria
um usuário novo. Siga o bootstrap do guia de deploy sem versionar senhas/hashes.
