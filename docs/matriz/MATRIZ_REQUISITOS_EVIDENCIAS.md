> Referência de desenho e governança importada do checkout versionado anterior.
> Não é novo aceite de capacidade ou validação externa. A estrutura executável
> atual está em [arquitetura](../ARCHITECTURE.md). Requisitos e propostas devem
> ser distinguidos de implementação e evidência datada.

# Matriz de requisitos e evidências — FISC

| Requisito | Evidência local | Classificação | Limitação |
|---|---|---|---|
| UI própria | `frontend` | Implementado | fluxo real depende de deployment |
| core desacoplado | `copilot-platform/packages/core`, `boundaries.toml` | Implementado | separação física concluída; dependências por release/hash |
| NF-e 55/4.00 | `context.py`, schemas nfe | Implementado | somente este recorte |
| XML seguro | `fiscal/xml_tools.py`, testes | Implementado | não prova segurança absoluta |
| XMLDSig | `fiscal/signature.py` | Implementado | cadeia ICP/LCR não verificada |
| base fiscal | `kb.py`, `dfe_kb` | Configurável | Qdrant/modelo/ingestão dependem do ambiente |
| revisão humana | `/incidents/{id}/review`, checkpoint | Configurável | PostgreSQL e Fernet necessários |
| REST/MCP/A2A/Eventos | `main.py`, `mcp`, `a2a`, `events` | Implementado | broker real não validado |
| regras por UF | `jurisdiction` no contexto | Não implementado | campo aceita UF, não é motor tributário |
| NFS-e/CT-e/MDF-e | não encontrados no plugin atual | Roadmap | criar plugins e schemas |
| autorização fiscal | não encontrada | Não implementado | FISC é read-only |
