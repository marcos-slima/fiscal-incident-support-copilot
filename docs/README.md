# Documentação do FISC

O código fiscal, UI, documentação e CI pertencem a este repositório. Core Python,
core-ui e operações pertencem à [Copilot Platform](https://github.com/marcos-slima/copilot-platform).
O IIC é outro consumidor; não é a localização atual do FISC ou da plataforma.

| Objetivo | Documento |
|---|---|
| Identidade, público e limites | [Identidade e escopo](IDENTIDADE_ESCOPO_FISC.md) |
| Utilizar o produto e interpretar resultados | [Manual](MANUAL_USUARIO_FISC.md) |
| Executar e configurar | [Deploy independente](DEPLOY.md) |
| Entender componentes e fluxo fiscal | [Arquitetura](ARCHITECTURE.md) |
| Identificar proprietário e caminhos | [Organização](ORGANIZACAO_DOCUMENTACAO.md) |
| Atualizar dependências | [Adoção da plataforma](ADOCAO_PLATAFORMA.md) |
| Preparar uma entrega | [Versionamento](VERSIONAMENTO_RELEASES.md), [índice](RELEASES.md), [modelo de notas](MODELO_NOTAS_RELEASE.md) |
| Consultar decisões fiscais | [Decisões](DECISOES.md) e [nome](DECISAO_NOME.md) |
| Identificar validações ainda necessárias | [Pendências](PENDENCIAS.md) |
| Consultar aceites, avaliação e extração anteriores | [Histórico](history/README.md) |
| Conferir todos os documentos | [Mapa documental](DOCUMENTATION_MAP.json) |

[Contribuição](../CONTRIBUTING.md) · [Apresentação](../README.md).
O escopo permanece NF-e 55/leiaute 4.00, read-only fiscal, com revisão humana.
Não há homologação fiscal ou validação operacional SAP/SEFAZ implícita.

[Política de manutenção documental](DOCUMENTATION_POLICY.md).

## Referências de arquitetura, processos e governança

Esses artefatos versionados no checkout anterior foram trazidos para o dono fiscal,
com [proveniência por hash/commit](REFERENCE_IMPORT.json). São referências de desenho,
não novos aceites de validação operacional.

- [Arquitetura de solução](ARQUITETURA_FISC.md) e [software](ARQUITETURA_SOFTWARE_FISC.md).
- [Processos](PROCESSOS_FISC.md), [governança IA](GOVERNANCA_IA_FISC.md) e [segurança](SEGURANCA_CONFORMIDADE_FISC.md).
- [Dossiê](DOSSIER_PRODUTO_FISC.md), [diagramas editáveis](diagramas/README.md).
- [Interfaces](matriz/MATRIZ_INTERFACES.md), [requisitos/evidências](matriz/MATRIZ_REQUISITOS_EVIDENCIAS.md),
  [riscos](matriz/MATRIZ_RISCOS.md) e [cartões Turbo EA](matriz/MATRIZ_CARTOES_TURBO_EA.md).

Os sete XMLs DrawIO/BPMN foram verificados estruturalmente; não houve execução
ou validação visual no Turbo EA. IDs propostos de cartões continuam propostos.


## Referências de arquitetura, governança e processo

Estes documentos foram recuperados do checkout versionado anterior. Requisitos,
propostas e estados de capacidade neles descritos não constituem novo aceite.

- [Arquitetura de solução](ARQUITETURA_FISC.md) e [arquitetura de software](ARQUITETURA_SOFTWARE_FISC.md).
- [Processos](PROCESSOS_FISC.md), [governança de IA](GOVERNANCA_IA_FISC.md) e [segurança/conformidade](SEGURANCA_CONFORMIDADE_FISC.md).
- [Dossiê de produto](DOSSIER_PRODUTO_FISC.md).
- [Interfaces](matriz/MATRIZ_INTERFACES.md), [requisitos/evidências](matriz/MATRIZ_REQUISITOS_EVIDENCIAS.md), [riscos](matriz/MATRIZ_RISCOS.md) e [cartões Turbo EA](matriz/MATRIZ_CARTOES_TURBO_EA.md).
- [Diagramas editáveis DrawIO/BPMN](diagramas/README.md).
- [Proveniência dos arquivos recuperados](REFERENCE_IMPORT.json).
