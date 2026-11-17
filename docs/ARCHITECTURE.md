# Arquitetura do FISC

Produto independente sobre bibliotecas versionadas de Copilot Platform.
Identificadores técnicos preservados: dfe-copilot, dfe_copilot, plugin dfe e @copilot/dfe-ui.

| Componente | Caminho atual / responsabilidade |
|---|---|
| Entrada | src/dfe_copilot/main.py: configura plugin, cookie dfe_session, KB e UI antes de carregar app.sdk |
| Contrato fiscal | src/dfe_copilot/context.py: família nfe, modelo 55, leiaute 4.00 e contexto validado |
| Plugin e ferramentas | src/dfe_copilot/plugin.py e fiscal/: XML, correlação e findings determinísticos |
| Recursos normativos | data/schemas e data/corpus; manifest/hashes preservados e dados incluídos no wheel |
| UI fiscal | frontend/src; build em frontend/dist, incluído no wheel pelo hook de build |
| KB fiscal | src/dfe_copilot/kb.py; coleção fiscal e ingestão explícita por deployment |
| Core e core-ui | dependências externas da plataforma, via app.sdk e índice público @copilot/core-ui |
| Operações | bundle copilot-operations, extraído em /opt/copilot-operations na imagem |
| Entrega e testes | Dockerfile, compose*.yaml, tests/, scripts/ e CI próprios |

O core não contém a implementação fiscal, e FISC não importa IIC.
shared-libraries.json e locks registram core 1.4.1, core-ui 0.1.1 e operações 1.0.0.
[Contratos compartilhados](https://github.com/marcos-slima/copilot-platform/blob/main/packages/core/docs/CONTRACTS.md)
HTTP/SDK 1.0 e plugin 1.1 não são os números de versão dos pacotes.

## Fluxo fiscal

1. A entrada configura DOMAIN_PLUGINS=dfe_copilot.plugin e serve o shell fiscal.
2. O contrato valida domain_context; contexto inválido retorna 422.
3. O plugin analisa bytes originais do XML, sem rede/DTD/entidades, confere XSD
   quando aplicável e conserva a proveniência/hashes das fontes.
4. Eventos são normalizados para UTC; regras distinguem retorno, timeout e reenvio.
   Timeout isolado não prova indisponibilidade da SEFAZ nem falha de processamento.
5. A KB fiscal pode produzir evidência ou lacuna explícita; sua disponibilidade
   depende da ingestão/configuração do deployment, não do sucesso do build.
6. O core incorpora findings e evidências. Explicação do LLM é hipótese, não fato.

O shell fiscal e os testes independentes estão implementados. Os 214 testes e
smoke de imagem da adoção passaram; isso não substitui revisão fiscal especializada,
validação de inferência real ou execução em SAP/SEFAZ. Resultados anteriores de
KB/avaliação são registros datados em [decisões](DECISOES.md) e [histórico](history/README.md).
[Execução](DEPLOY.md) · [manual](MANUAL_USUARIO_FISC.md) · [pendências](PENDENCIAS.md).
