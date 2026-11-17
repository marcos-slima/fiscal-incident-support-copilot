# Organização documental e fontes oficiais

| Proprietário | Conteúdo canônico |
|---|---|
| FISC | Código src/dfe_copilot, frontend, contratos fiscais, XML/XSD, decisões e guias fiscais, testes, CI e imagem |
| Copilot Platform | Core Python, core-ui, SDK/HTTP/plugins, operações, DAs e testes comuns |
| IIC | Shell e UI de integração, implantação e testes do consumidor IIC |

[Índice FISC](README.md) · [índice da plataforma](https://github.com/marcos-slima/copilot-platform/blob/main/docs/README.md)
· [índice IIC](https://github.com/marcos-slima/integration-incident-copilot/blob/master/docs/README.md).

Guias atuais ficam em docs/; aceites, estudo inicial, pré-extração e avaliação
anteriores ficam em [history/](history/README.md), com origem/commit. URLs antigas
recebem páginas de compatibilidade. Decisões fiscais mantêm a cronologia e os
limites de cada medição; não são confirmação automática da versão atual.
O [mapa documental](DOCUMENTATION_MAP.json) classifica todos os Markdown de produto.

O frontend tem [guia próprio](../frontend/README.md). Diagramas e APIs fiscais
usam caminhos deste repositório; links de implementação comum apontam para a plataforma.
Não manter um segundo manual de instalação do core no FISC.
O [guia de adoção](ADOCAO_PLATAFORMA.md) e a [política](VERSIONAMENTO_RELEASES.md)
registram versões/hashes independentes. Dados de clientes, segredos e relatórios
operacionais não pertencem ao Git.
