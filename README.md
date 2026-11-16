# FISC — Fiscal Incident Support Copilot

**Diagnóstico assistido de incidentes de NF-e, com fatos, hipóteses e evidências para revisão humana.**

O FISC apoia equipes **SAP AMS N2/N3** na investigação de incidentes de
**NF-e modelo 55, leiaute 4.00**. Combina verificações determinísticas de XML e
eventos, recuperação de referências fiscais e explicação assistida por IA
para organizar a investigação e orientar o próximo passo.

> **Maturidade:** MVP em construção, com avaliação baseada em casos sintéticos.
> Não há homologação fiscal ou validação operacional em SAP/SEFAZ reais.
> O produto analisa documentos e sistemas fiscais em modo read-only; a decisão
> e a execução de qualquer ação fiscal permanecem com pessoas autorizadas.

[Identidade e escopo](docs/IDENTIDADE_ESCOPO_FISC.md) ·
[Documentação técnica](docs/README.md) ·
[Código-fonte](https://github.com/marcos-slima/integration-incident-copilot/tree/feat/dfe-runtime-existing-kb/packages/dfe) ·
[Execução e configuração](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/docs/DEPLOY.md)

## Por que o FISC existe

Um timeout seguido de rejeição por duplicidade não explica, sozinho, a causa
do incidente. É preciso relacionar o retorno, a chave do documento e a linha
do tempo, verificar o XML e identificar quais informações ainda faltam.

O FISC organiza essa investigação e distingue o que foi observado do que é
hipótese. O benefício esperado é reduzir o esforço de triagem e tornar a
análise rastreável; ganhos de tempo e precisão em produção ainda precisam
ser medidos.

## O que você pode investigar

| Situação | Apoio oferecido |
|---|---|
| Duplicidade — `cStat 204` | Examina o retorno e a linha do tempo para avaliar a hipótese de reenvio após timeout do mesmo documento |
| Divergência de chave — `cStat 539` | Organiza achados conforme a regra de correlação implementada |
| Timeout sem retorno | Explicita o resultado desconhecido e as verificações necessárias antes de decidir por reenvio |
| Dúvidas sobre o XML recebido | Verifica parse, chave, protocolo, XSD quando aplicável e integridade XMLDSig no perfil suportado |
| Necessidade de fundamentação | Recupera referências da base fiscal quando disponível e apresenta fontes e lacunas |

Interpretar outros códigos de retorno não significa possuir diagnóstico
especializado para toda rejeição. Um XML válido no XSD também não comprova
validade tributária, autorização ou confiança da cadeia do certificado.

## Exemplo de investigação

**Cenário ilustrativo, sem execução neste README:** a operação informa que
uma NF-e sofreu timeout e retornou `cStat 204` após um novo envio.

1. O analista fornece a descrição, o XML de retorno disponível, o ambiente,
   a UF e os eventos relacionados explicitamente à mesma chave de acesso.
2. As ferramentas verificam o XML e extraem o retorno. A regra de correlação
   procura dois ou mais envios do mesmo documento com timeout entre eles.
3. O resultado distingue o **fato** de existir retorno 204 da **hipótese** de
   reenvio após timeout. Sem os eventos necessários, registra a lacuna em vez
   de afirmar essa causa.
4. O analista revisa as evidências e realiza a verificação autorizada da
   situação do documento antes de decidir por uma ação operacional.

O FISC não consulta a SEFAZ nem reenvia a NF-e automaticamente. Uma hipótese
produzida pelo LLM não confirma a causa.

Para o contrato de entrada e um exemplo de requisição, consulte o
[README técnico do produto](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/README.md). Os cenários de demonstração são sintéticos.

## Arquitetura resumida

```mermaid
flowchart TB
    U[Analista AMS N2/N3] --> F[FISC: interface e API do produto]
    F --> C[Core Python: SDK e orquestração]
    C --> P[Plugin fiscal: XML e correlação]
    C --> K[RAG e base fiscal quando disponíveis]
    C --> L[Gateway LLM: explicação assistida]
    P --> E[Fatos, hipóteses, referências e lacunas]
    K --> E
    L --> E
    E --> R[Revisão humana]
    UI[Core UI: componentes compartilhados] --> F
```

O **FISC** possui domínio, interface e ponto de entrada próprios.
O **Integration Incident Copilot (IIC)** é o produto de diagnóstico de
integrações empresariais. Ambos reutilizam `copilot-core` e
`@copilot/core-ui`; um produto não importa o outro.

O compartilhamento preserva serviços de gateway LLM, RAG, evidências,
autenticação e infraestrutura. As regras e fontes fiscais permanecem no FISC.
Consulte os [contratos públicos do core](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/core/docs/CONTRACTS.md).

## Onde está a implementação

Este repositório apresenta o FISC e seu escopo. **A implementação é mantida
atualmente no [monorepo Integration Incident Copilot](https://github.com/marcos-slima/integration-incident-copilot), em
[`packages/dfe`](https://github.com/marcos-slima/integration-incident-copilot/tree/feat/dfe-runtime-existing-kb/packages/dfe).** A configuração e o build ainda usam esse workspace.

Os links técnicos desta edição apontam para a branch
`feat/dfe-runtime-existing-kb`, usada como referência de implementação.

| Elemento | Identificador preservado |
|---|---|
| Distribuição Python | `dfe-copilot` |
| Módulo Python | `dfe_copilot` |
| Plugin de domínio | `dfe` |
| Shell de interface | `@copilot/dfe-ui` |
| Imagem e variáveis | `dfe-copilot` e prefixos `DFE_`/`dfe_` |

FISC é a marca do produto. Esses nomes técnicos permanecem para preservar
compatibilidade de imports, builds e configurações.

## Como experimentar

Use o checkout do **monorepo**, com Python 3.12+, uv e os serviços/modelos
configurados. A interface exige build e credenciais de acesso; a configuração
completa está no [guia de execução](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/docs/DEPLOY.md).

Para desenvolvimento, a partir da raiz do monorepo já configurado:

```bash
uv sync --locked --all-packages
npm ci
npm run build -w @copilot/dfe-ui
uv run --package dfe-copilot python -m uvicorn dfe_copilot.main:app --reload --port 8001
```

A entrada continua sendo `dfe_copilot.main:app`. O guia também descreve
Docker Compose, primeiro acesso, Ollama, base fiscal e ingestão. Os comandos
acima não configuram credenciais nem provisionam modelos e infraestrutura.

## Maturidade e limites

| Aspecto | Situação |
|---|---|
| Domínio fiscal | NF-e 55, leiaute 4.00; regras especializadas de duplicidade, divergência de chave e timeout |
| UI, empacotamento e imagem | Implementados, com verificações locais históricas registradas |
| Testes e avaliação | Casos sintéticos; aceites locais não substituem validação fiscal externa |
| CI | Workflow específico no monorepo; esta apresentação não atesta resultado remoto atual |
| Base fiscal e revisão persistente | Dependem dos serviços e da configuração do ambiente |
| Revisão especializada | Pendente conforme o registro de pendências |
| SAP/SEFAZ reais e homologação | Não comprovados pelos aceites citados |

O contrato aceita UFs e ambientes de homologação/produção, mas essa aceitação
não comprova cobertura normativa por UF nem prontidão operacional nesses
ambientes. A verificação de integridade XMLDSig não inclui confiança completa
ICP-Brasil, cadeia e revogação.

O limite read-only se aplica aos documentos e sistemas fiscais. Diagnósticos,
revisões humanas e dados operacionais podem ser persistidos conforme a
configuração.

Estão fora do escopo atual: suporte completo a NFC-e, NFS-e, CT-e e MDF-e;
cálculo tributário completo; consulta direta à SEFAZ; emissão, autorização,
retransmissão, cancelamento, inutilização e execução de contingência.

## Versionamento e entregas

FISC, IIC, core Python e core-ui seguem versões independentes. Consulte a
[política de releases](docs/VERSIONAMENTO_RELEASES.md) e o
[índice de entregas do FISC](docs/RELEASES.md). A versão declarada no manifest
não comprova disponibilidade de pacote ou imagem publicados.

## Validação fora do monorepo

Em 2026-11-16, um perfil externo passou em 214 testes fiscais em Python 3.12
e em 214 testes em Python 3.14, além de build da UI, wheel e smoke da imagem.
Foram usados artefatos compartilhados aprovados no CI, sem fontes ou ambiente
do core/IIC. Veja o [relatório e seus limites](docs/VALIDACAO_FORA_MONOREPO.md).
Isso não constitui publicação em registro ou homologação fiscal.

## Documentação e próximos passos

Consulte o [mapa de fontes oficiais](docs/ORGANIZACAO_DOCUMENTACAO.md) e o
[guia de contribuição](CONTRIBUTING.md) para saber onde propor cada alteração.

| Preciso de… | Consulte |
|---|---|
| Posicionamento e fronteiras do produto | [Identidade e escopo](docs/IDENTIDADE_ESCOPO_FISC.md) |
| Orientação de uso e revisão | [Manual do usuário](docs/MANUAL_USUARIO_FISC.md) |
| Instalação, credenciais e serviços | [Guia de execução](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/docs/DEPLOY.md) |
| Arquitetura, processos e governança | [Índice documental](docs/README.md) |
| Contrato de entrada e requisição de exemplo | [README técnico](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/README.md) |
| Restrições e validações pendentes | [Pendências](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/docs/PENDENCIAS.md) |
| Evidência histórica de testes locais | [Aceite P2](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/docs/ACEITE_P2.md) e [aceite P6](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/docs/ACEITE_P6.md) |
| Licença da implementação | [Licença MIT](LICENSE) |

A evolução prevê consolidar a apresentação própria, organizar releases por
produto e distribuir as bibliotecas compartilhadas. A extração do código para
outro repositório depende dessa preparação e de uma decisão posterior.

Use as [issues deste repositório](https://github.com/marcos-slima/fiscal-incident-support-copilot/issues)
para dúvidas e problemas do FISC. Alterações de código continuam no
[monorepo](https://github.com/marcos-slima/integration-incident-copilot).
Ao relatar problemas, use dados sintéticos ou anonimizados e preserve o
contexto necessário para reproduzir o caso.
