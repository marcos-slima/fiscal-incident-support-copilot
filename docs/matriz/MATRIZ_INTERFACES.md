> Referência de desenho e governança importada do checkout versionado anterior.
> Não é novo aceite de capacidade ou validação externa. A estrutura executável
> atual está em [arquitetura](../ARCHITECTURE.md). Requisitos e propostas devem
> ser distinguidos de implementação e evidência datada.

# Matriz de interfaces — FISC

| Interface | Chamador | Entrada | Auth | Saída | Escrita externa | Evidência |
|---|---|---|---|---|---|---|
| UI | usuário | descrição/XML/contexto | sessão web | diagnóstico | não | `frontend/src` |
| REST sync | sistema | `IncidentRequest` | `X-API-Key` | `DiagnosisResponse` | não | [`app/main.py::diagnose`](https://github.com/marcos-slima/copilot-platform/blob/main/packages/core/src/app/main.py) |
| REST async | sistema | `IncidentRequest` | `X-API-Key` | `job_id`/resultado | fila interna | [`app/queue.py`](https://github.com/marcos-slima/copilot-platform/blob/main/packages/core/src/app/queue.py) |
| MCP | agente | `diagnose_incident` | `X-API-Key` | resultado da tool | não | [`app/mcp/server.py`](https://github.com/marcos-slima/copilot-platform/blob/main/packages/core/src/app/mcp/server.py) |
| A2A | agente | JSON-RPC | `X-A2A-Api-Key` | task | task store | [`app/a2a/server.py`](https://github.com/marcos-slima/copilot-platform/blob/main/packages/core/src/app/a2a/server.py) |
| CloudEvents | monitor | CE 1.0 | Event Mesh key | `202` | diagnóstico interno | [`app/events/consumer.py`](https://github.com/marcos-slima/copilot-platform/blob/main/packages/core/src/app/events/consumer.py) |
| AMQP | broker | CE 1.0 | configuração AMQP | task/log | diagnóstico interno | `amqp_consumer.py` |
| Health | orquestrador | nenhum | público/detalhe protegido | status | não | `main.py` |
| Discovery | shell/agente | nenhum | API key/sessão | plugins/schema | não | `/domain-plugins` |

NFS-e, CT-e e MDF-e não possuem contratos fiscais específicos implementados no
estado atual.
