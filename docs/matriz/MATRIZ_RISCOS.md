> Referência de desenho e governança importada do checkout versionado anterior.
> Não é novo aceite de capacidade ou validação externa. A estrutura executável
> atual está em [arquitetura](../ARCHITECTURE.md). Requisitos e propostas devem
> ser distinguidos de implementação e evidência datada.

# Matriz de riscos — FISC

| ID | Risco | Prob. | Impacto | Controle | Residual |
|---|---|---:|---:|---|---|
| R-01 | hipótese apresentada como fato | M | A | findings tipados e revisão | M |
| R-02 | regra fiscal fora da vigência | M | A | versão, fonte e vigência | M |
| R-03 | diferença entre UFs | A | A | lacuna e roadmap de rule packs | A |
| R-04 | XML com XXE/DTD | B | A | parser local sem rede | B |
| R-05 | vazamento de PII a LLM | M | A | soberania, redaction e gateway | M |
| R-06 | chave exposta | M | A | env/cifrado/rotação | M |
| R-07 | revisão sem checkpoint | M | M | `can_resume=false` explícito | B |
| R-08 | tenant sem escopo | M | A | `tenant_id` e filtros | A |
| R-09 | dependência indisponível | M | M | readiness, timeout, breaker | B |
| R-10 | confiança de recuperação confundida com precisão | M | A | métricas separadas | B |
| R-11 | integração externa não comprovada | M | A | rótulo de evidência | M |

Probabilidade/impacto são avaliação qualitativa de arquitetura e exigem revisão
do responsável de risco no Turbo EA.
