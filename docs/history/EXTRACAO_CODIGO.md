# Registro histórico — EXTRACAO_CODIGO.md

> Snapshot anterior à organização documental de 2026-11-17. Não usar como
> instrução de instalação atual. Origem: [arquivo e commit](https://github.com/marcos-slima/fiscal-incident-support-copilot/blob/b34e8a6a89dabe8bd98e5b3bf919bc3baf2e4d9d/docs/EXTRACAO_CODIGO.md).
> Links relativos foram fixados no snapshot de origem; comandos antigos são evidência histórica.

# Extração do código FISC

Decisão executada em 2026-11-16: o repositório FISC passa a ser a fonte oficial
de implementação e documentação do produto. A validação da etapa 9 demonstrou
build/testes/execução independentes; a distribuição permanente das bibliotecas
resolve a dependência de artefatos temporários de CI.

## Histórico preservado

Foram separados 25 commits do caminho packages/dfe da branch de implementação
do IIC usando git subtree split. Autores, datas e mensagens desse histórico
foram mantidos, com SHAs reescritos pela mudança de raiz. A branch extraída
termina em 4d7844652d25990e5bcd7b245347f92d7b92e89a e é unida ao histórico
documental existente do FISC por merge, sem squash.

A origem de código validada na etapa 9 foi o snapshot
43d614476973e648c5dda253eac46c2bdb6bbc0f. Regras anteriores à criação do caminho
packages/dfe permanecem rastreáveis no histórico original do IIC. O histórico
do IIC não foi reescrito nem apagado.

## Fronteiras e distribuição

O FISC mantém src, frontend, tests, data, scripts, Docker/Compose e CI.
Copilot-core e core-ui permanecem no IIC e são consumidos por URLs permanentes:

- [Core 1.4.0](https://github.com/marcos-slima/integration-incident-copilot/releases/tag/core/v1.4.0)
- [Core UI 0.1.0](https://github.com/marcos-slima/integration-incident-copilot/releases/tag/core-ui/v0.1.0)

Hashes estão em shared-libraries.json, uv.lock e frontend/package-lock.json.
Nenhuma fonte de core/IIC é incorporada ao repositório FISC. O pacote
operacional de migrações do core é baixado com verificação de hash na imagem.

Os identificadores técnicos e versões atuais foram preservados. As próximas
tags/release de produto FISC pertencem a este repositório; não foi criada uma
release de produto apenas para representar a migração.

## Transição do monorepo

O snapshot histórico packages/dfe no IIC não é mais fonte de evolução do
produto. Não remover esse diretório enquanto os PRs 24, 25 e 26 e seus
workspaces/pipelines ainda o referenciam. A retirada física requer atualização
coordenada desses consumidores e dos testes de fronteira; fazê-la isoladamente
quebraria builds do IIC. O core continua compartilhado sem sincronização por cópia.

PRs de implementação fiscal vão ao FISC; mudanças compartilhadas vão ao IIC.
Documentos históricos e aceites anteriores podem citar os caminhos antigos.
Eles são registros da época, não instruções atuais de execução.

A validação usa dados sintéticos. A extração não significa homologação fiscal,
integração SAP/SEFAZ real, inferência LLM medida ou deploy em produção.
