> Referência de desenho e governança importada do checkout versionado anterior.
> Não é novo aceite de capacidade ou validação externa. A estrutura executável
> atual está em [arquitetura](../ARCHITECTURE.md). Requisitos e propostas devem
> ser distinguidos de implementação e evidência datada.

# Diagramas FISC — DrawIO e BPMN

Os arquivos-fonte são separados por notação:

- `drawio/`: arquitetura, componentes, confiança, deployment, interfaces,
  auditoria e evolução;
- `bpmn/`: processos, participantes, tarefas, gateways, eventos e exceções.

Os cartões Turbo EA referenciados são identificadores propostos e marcados como
“a registrar” quando não há cartão real disponível no checkout.

## DrawIO

| Arquivo | Objetivo | Visões cobertas |
|---|---|---|
| `fisc_context_and_c4.drawio` | contexto empresarial e C4 | contexto, sistema, containers |
| `fisc_data_security.drawio` | dados e confiança | fluxo, trust boundaries, soberania, segurança |
| `fisc_deployment_and_interfaces.drawio` | execução e integração | deployment, interfaces, auditoria |
| `fisc_human_review_and_evolution.drawio` | revisão e evolução | HITL, NFS-e/CT-e/MDF-e |

As linhas sólidas representam chamadas síncronas; tracejadas representam
eventos. Cada aresta traz o protocolo quando conhecido.

## BPMN 2.0

| Arquivo | Processos modelados |
|---|---|
| `fisc_request_channels.bpmn` | manual, REST síncrono/assíncrono, MCP, A2A, CloudEvents, AMQP |
| `fisc_diagnosis_and_review.bpmn` | triagem, XML inválido, base fiscal, revisão, escalonamento, encerramento |
| `fisc_governance_and_security.bpmn` | indisponibilidade, mudança fiscal, fontes/vigência, incidente de segurança |

Os BPMN são modelos de processo, não evidência de execução em ambiente externo.
