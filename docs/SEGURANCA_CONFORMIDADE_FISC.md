> Referência de desenho e governança importada do checkout versionado anterior.
> Não é novo aceite de capacidade ou validação externa. A estrutura executável
> atual está em [arquitetura](ARCHITECTURE.md). Requisitos e propostas devem
> ser distinguidos de implementação e evidência datada.

# Segurança e conformidade — FISC

## 1. Superfícies de autenticação

| Superfície | Controle | Estado |
|---|---|---|
| UI | usuário/senha, cookie `HttpOnly`, `SameSite=Strict`, `SESSION_SECRET` | Implementado |
| REST | `X-API-Key` | Implementado |
| A2A | `X-A2A-Api-Key` | Implementado |
| Eventos | `X-Event-Mesh-Api-Key` | Implementado |
| MCP | `X-API-Key` via middleware | Implementado |
| Administração | chave administrativa dedicada | Implementado |

As chaves devem ser diferentes entre IIC, FISC, ambientes e superfícies. Em
produção, `REQUIRE_AUTH=true` deve impedir inicialização sem configuração
explícita.

## 2. Segredos

- não versionar `.env`, senha, hash, token ou certificado;
- rotacionar chaves após suspeita de exposição;
- usar armazenamento cifrado para credenciais persistentes;
- não imprimir valores nos logs;
- separar `SESSION_SECRET`, API keys e chave Fernet de credenciais LLM.

## 3. XML e entrada não confiável

O parser fiscal recusa DTD, entidades externas, rede e XML acima do limite de
payload. O XML original não é reescrito; o hash é calculado sobre os bytes
recebidos. XML bem-formado não significa conformidade XSD, assinatura válida ou
autorização.

## 4. Autorização e ações

O FISC atual é read-only para o domínio fiscal. MCP usa capability registry
fail-closed. A revisão humana altera o estado interno/checkpoint; não autoriza
cancelamento, reenvio, inutilização, contingência ou alteração em SAP/SEFAZ.

## 5. Disponibilidade e abuso

- rate limiting por IP;
- timeout por chamada e por diagnóstico;
- circuit breaker em conectores/gateway;
- `/health` para liveness;
- `/ready` para dependências configuradas;
- resposta 503 quando a dependência obrigatória está degradada;
- idempotência para eventos CloudEvents.

## 6. Isolamento

IIC e FISC usam shells, imagens, cookies e segredos próprios. O core não importa
produtos. O isolamento por tenant é parcial no estado atual: ausência de
`tenant_id` explícito não é fronteira de autorização. Isso deve ser corrigido
antes de oferecer multi-tenancy como garantia.

## 7. Auditoria e retenção

Preservar, conforme a política da organização:

- `incident_id` e correlação;
- versão do contrato, prompt, modelo e corpus;
- evidências e locators;
- decisão de revisão humana;
- `error_id` de falhas;
- timestamp, ator e ambiente.

Definir retenção por classe de dado e direito de eliminação antes da operação
com documentos reais. O repositório não comprova uma política legal universal.

## 8. Riscos principais

| Risco | Controle atual | Limite |
|---|---|---|
| prompt injection | fatos separados, capability registry, read-only | não elimina erro de interpretação |
| vazamento de PII | redaction/política de soberania | regex não é defesa completa |
| fonte desatualizada | manifesto, versão e vigência | curadoria humana continua necessária |
| regra estadual incorreta | lacuna sem fonte aplicável | motor completo por UF não implementado |
| credencial exposta | chaves fora do código e rotação | operação deve executar rotação |
| falsa certeza | `diagnosis_confidence` e revisão | decisão fiscal continua humana |

## 9. Cartões Turbo EA

| Elemento | Cartão proposto | Estado |
|---|---|---|
| Controle de acesso | `FISC-CTRL-SEC-01` | a registrar |
| Limite de confiança | `FISC-CTRL-SEC-02` | a registrar |
| Proteção XML | `FISC-CTRL-SEC-03` | a registrar |
| Soberania de dados | `FISC-CTRL-DATA-01` | a registrar |
| Risco de prompt injection | `FISC-RISK-AI-01` | a registrar |
