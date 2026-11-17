> Referência de desenho e governança importada do checkout versionado anterior.
> Não é novo aceite de capacidade ou validação externa. A estrutura executável
> atual está em [arquitetura](ARCHITECTURE.md). Requisitos e propostas devem
> ser distinguidos de implementação e evidência datada.

# Dossiê do produto — Fiscal Incident Support Copilot (FISC)

## 1. Resumo executivo

O FISC é um copiloto de suporte para incidentes de documentos fiscais
eletrônicos. Ele combina validações determinísticas e explicação assistida por
LLM para reduzir o tempo de triagem, preservar evidências e orientar o próximo
passo sem automatizar decisões fiscais.

## 2. Problema

Incidentes fiscais costumam envolver XML, retornos da SEFAZ, protocolos,
mensageria, ambientes, UF, versões de schema e linhas do tempo incompletas. A
investigação manual mistura fato observado, regra normativa e hipótese, o que
dificulta auditoria e repetibilidade.

## 3. Proposta de valor

- separar fatos de hipóteses;
- validar XML sem alterar a entrada;
- preservar hash e proveniência;
- recuperar fonte fiscal aplicável;
- correlacionar timeout, reenvio e retorno;
- oferecer UI e interfaces para automação;
- manter revisão humana e limites read-only.

## 4. Produto atual

### Implementado

- UI própria do FISC;
- login por sessão;
- REST síncrono e assíncrono;
- MCP, A2A e CloudEvents;
- plugin fiscal versionado;
- NF-e modelo 55, leiaute 4.00;
- validação segura de XML e XSD local;
- chave de acesso, `cStat`, protocolo e XMLDSig;
- base fiscal `dfe_kb` opcional;
- fatos × hipóteses e proveniência;
- revisão humana persistente opcional;
- imagem Docker e CI próprios;
- exemplos Python e TypeScript.

### Não declarar como capacidade atual

- NFS-e, CT-e ou MDF-e completos;
- cálculo tributário completo por UF;
- consulta direta à SEFAZ;
- autorização, cancelamento, inutilização ou contingência;
- confiança ICP-Brasil completa, LCR ou OCSP;
- homologação fiscal ou integração SAP real sem evidência específica.

## 5. Público e casos de uso

| Público | Uso |
|---|---|
| AMS N2/N3 | triagem e investigação inicial |
| especialista fiscal | revisão de regra, evidência e decisão |
| integração SAP | solicitação por REST, evento, A2A ou MCP |
| operação | health, readiness, filas e observabilidade |
| arquitetura/segurança | fronteiras, soberania e auditoria |

## 6. Demonstração recomendada

1. apresentar um XML sintético completo;
2. demonstrar fato de XSD/chave/protocolo;
3. demonstrar hipótese de duplicidade após timeout;
4. mostrar evidências e lacunas;
5. editar ou rejeitar a hipótese em revisão humana;
6. mostrar que nenhuma ação fiscal é executada;
7. executar o mesmo caso via REST e via cliente TypeScript;
8. consultar `/ready` e `/domain-plugins`.

## 7. Segurança e confiança

O FISC adota autenticação separada por superfície, parser sem rede, chaves fora
do código, política de soberania do LLM e resposta com procedência. O produto é
um sistema de suporte à decisão, não um autorizador fiscal.

## 8. Indicadores sugeridos

Os indicadores devem medir o processo, não apenas a resposta do LLM:

- tempo até a primeira triagem;
- percentual de casos com XML e protocolo;
- percentual de diagnósticos com evidência `system_observed`;
- taxa de `G-*` por tipo de ausência;
- tempo até revisão humana;
- reabertura ou divergência após decisão humana;
- sucesso de entrega por interface;
- latência e erro por dependency.

Hit@k de recuperação não é precisão do diagnóstico. Benchmark de modelo não é
prova de validade fiscal.

## 9. Roadmap arquitetural

1. fechar matriz fiscal por UF, vigência e fonte normativa;
2. criar plugins separados para NFS-e, CT-e e MDF-e;
3. implementar validadores determinísticos de cálculos com tolerância e
   evidência;
4. validar integração real somente leitura com ambientes autorizados;
5. completar isolamento multi-tenant e retenção por classe de dado;
6. separar fisicamente repositórios e publicar pacotes do core;
7. reexecutar CI e avaliações por produto após a separação.

## 10. Mensagem de apresentação

> O FISC transforma um incidente fiscal em uma investigação rastreável: as
> ferramentas verificam o documento e suas evidências, o modelo explica
> hipóteses, e o time fiscal mantém a decisão operacional.

## 11. Evidência e limites

Este dossiê descreve o estado do checkout local e os contratos implementados.
Não constitui prova de operação em tenant SAP, broker Event Mesh, SEFAZ,
prefeitura, CT-e ou MDF-e. Cada implantação deve anexar sua própria evidência
de configuração, conectividade, segurança e validação fiscal.
