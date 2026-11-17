> Referência de desenho e governança importada do checkout versionado anterior.
> Não é novo aceite de capacidade ou validação externa. A estrutura executável
> atual está em [arquitetura](../ARCHITECTURE.md). Requisitos e propostas devem
> ser distinguidos de implementação e evidência datada.

# Matriz de cartões Turbo EA — FISC

Não foram encontrados no checkout IDs confirmados de cartões Turbo EA. A tabela
abaixo é um mapa de trabalho para cadastro; não é inventário já sincronizado.

| Tipo Turbo EA | ID de trabalho | Nome | Relacionamentos |
|---|---|---|---|
| Application | `FISC-APP-01` | FISC API/UI | usa core; expõe plugin dfe |
| Application | `IIC-APP-01` | Integration Incident Copilot | usa core; separado do FISC |
| IT Component | `CORE-COMP-01` | copilot-platform/packages/core | suporta IIC e FISC |
| IT Component | `COREUI-COMP-01` | @copilot/core-ui | shells de UI |
| IT Component | `DFE-PLUGIN-01` | plugin dfe | valida contexto/XML |
| Data Object | `FISC-DATA-01` | XML/DiagnosisResponse | entrada/saída |
| Data Object | `FISC-KB-01` | dfe_kb | fonte recuperada |
| Technology Service | `FISC-TS-01` | LLM Gateway | provider configurável |
| External System | `FISC-EXT-01` | Ollama | provider local |
| External System | `FISC-EXT-02` | OpenAI/Azure OpenAI | opcional, sujeito à política |
| Business Process | `FISC-BP-01` | Diagnosticar incidente fiscal | UI/API/evento |
| Business Process | `FISC-BP-02` | Revisar diagnóstico | humano/checkpoint |
| Business Capability | `FISC-CAP-01` | Suporte à decisão fiscal | read-only |
| Control | `FISC-CTRL-01` | Evidência antes da hipótese | findings/evidence |
| Risk | `FISC-RISK-01` | Regra fora de vigência | matriz de riscos |
| Business Actor | `FISC-ACTOR-01` | Analista fiscal/AMS | solicita/revisa |
| Organization | `FISC-ORG-01` | Operação fiscal | governa fontes e decisão |
| Decision | `FISC-DEC-01` | Evidência suficiente? | segue ou escala |
