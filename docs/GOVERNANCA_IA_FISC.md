> Referência de desenho e governança importada do checkout versionado anterior.
> Não é novo aceite de capacidade ou validação externa. A estrutura executável
> atual está em [arquitetura](ARCHITECTURE.md). Requisitos e propostas devem
> ser distinguidos de implementação e evidência datada.

# Governança de IA — FISC

## 1. Princípio de responsabilidade

O FISC é um sistema de suporte à decisão. Ferramentas determinísticas produzem
fatos; o LLM sintetiza hipóteses; a decisão fiscal e qualquer ação operacional
continuam com pessoas autorizadas.

| Classificação | Origem | Pode confirmar causa? |
|---|---|---|
| Fato | parser, XSD, chave, protocolo, regra ou conector | somente no escopo da ferramenta |
| Evidência | fonte recuperada com `source_id`, `locator` e hash | sustenta análise, não prova violação isoladamente |
| Hipótese | LLM ou correlação não determinística | não; exige revisão |
| Lacuna | ausência/indisponibilidade de evidência | reduz confiança |

## 2. Ciclo de vida do prompt

1. definir persona e escopo fiscal;
2. versionar prompt no produto;
3. registrar digest e `prompt_version` na resposta;
4. medir em dataset separado de desenvolvimento, validação e blind;
5. revisar regressões e casos controversos;
6. publicar somente após aprovação do responsável técnico e fiscal;
7. manter versão anterior para rollback.

O prompt não pode instruir o modelo a inventar fonte, afirmar autorização ou
executar ação fiscal.

## 3. Ciclo de vida da base fiscal

```text
fonte autorizada → manifesto/hash → ingestão idempotente → filtros de domínio
→ recuperação → evidência com locator → revisão → histórico/rollback
```

O filtro deve considerar, quando disponível: produto, modelo, leiaute,
jurisdição, município, ambiente, vigência e código de retorno. Score de
recuperação mede ordenação; não mede precisão fiscal ou acerto do diagnóstico.

## 4. Dataset e avaliação

O dataset sintético atual possui casos de NF-e e regressão offline. A avaliação
deve separar:

- validade estrutural do XML;
- acerto de fatos determinísticos;
- qualidade de recuperação;
- qualidade da hipótese;
- calibração de `diagnosis_confidence`;
- decisão após revisão humana.

Hit@k, MRR ou score de reranking não devem ser apresentados como precisão
tributária. A validação cega deve registrar modelo, prompt, corpus, versão e
ambiente.

## 5. Soberania e sensibilidade

- `strict`: dados confidenciais permanecem em provider local, como Ollama;
- `cloud_with_dlp`: cloud somente quando a política permitir e PII já tiver
  sido redigida;
- segredo, certificado e chave privada nunca entram no prompt;
- a política efetiva deve ser consultável e auditável.

## 6. Operação e monitoramento

Monitorar:

- latência por etapa;
- custo estimado e orçamento por diagnóstico;
- circuit breaker e indisponibilidade;
- taxa de lacunas;
- evidência observada versus simulada;
- revisão humana e divergência posterior;
- alterações de prompt, modelo e corpus.

## 7. Rollback

Rollback de prompt, modelo ou corpus deve identificar a versão anterior e não
apagar o histórico. O conteúdo efetivamente servido deve ser reconferido após
rollback; alterar apenas uma tabela relacional não prova que os vetores também
foram restaurados.

## 8. Cartões Turbo EA

| Elemento | Cartão proposto | Estado |
|---|---|---|
| Governança de IA | `FISC-CTRL-AI-01` | a registrar no Turbo EA |
| Prompt fiscal | `FISC-DATA-PROMPT-01` | a registrar |
| Base fiscal | `FISC-DATA-KB-01` | a registrar |
| Avaliação | `FISC-PROC-AI-EVAL-01` | a registrar |
| Revisão humana | `FISC-CTRL-HITL-01` | a registrar |

Não há no checkout evidência de IDs reais de cartões Turbo EA; os códigos acima
são identificadores de trabalho, não inventário confirmado.
