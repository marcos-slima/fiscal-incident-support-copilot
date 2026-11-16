# Identidade e escopo — Fiscal Incident Support Copilot (FISC)

Data: 2026-11-16. Estado: base de posicionamento para revisão do responsável pelo produto.

Este documento consolida a identidade e o recorte existentes. Não amplia o
contrato fiscal nem representa homologação, aprovação de especialista ou
validação em produção. Orienta a futura apresentação própria no GitHub.

## 1. Identidade

| Elemento | Definição |
|---|---|
| Nome formal | Fiscal Incident Support Copilot |
| Marca | FISC |
| Categoria | Copiloto de suporte à investigação de incidentes fiscais |
| Frase de apresentação | Diagnóstico assistido de incidentes de NF-e, com fatos, hipóteses e evidências para revisão humana. |
| Público principal | Analistas e especialistas de suporte SAP AMS N2/N3 que investigam incidentes de NF-e |
| Público complementar | Especialistas fiscais, equipes de integração, operação, arquitetura e segurança |
| Estágio | MVP em construção, com avaliação baseada em casos sintéticos e limitações de validação externa |

O nome e a regra de uso seguem a [decisão de identidade](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/docs/DECISAO_NOME.md).
FISC é a marca de comunicação. `dfe-copilot`, `dfe_copilot`, plugin `dfe`,
`@copilot/dfe-ui` e os prefixos técnicos existentes permanecem preservados.

## 2. Problema e proposta de valor

A investigação de um incidente fiscal exige reunir XML, protocolo, código de
retorno, contexto de ambiente e eventos de transmissão. Entradas incompletas
ou divergentes dificultam distinguir o retorno observado da hipótese sobre
sua causa e decidir o que verificar antes de um novo envio.

O FISC reúne essas entradas, aplica verificações determinísticas, consulta a
base fiscal quando disponível e apresenta fatos, hipóteses, referências e
lacunas. A explicação por LLM apoia a investigação; a confirmação da causa e a
decisão operacional permanecem com pessoas autorizadas.

O benefício esperado é reduzir esforço de triagem e melhorar a rastreabilidade.
Não há, neste documento, comprovação de redução de tempo, precisão diagnóstica
em produção ou retorno financeiro.

## 3. Relação com IIC e core compartilhado

| Componente | Responsabilidade |
|---|---|
| FISC | Contexto e ferramentas fiscais, regras de correlação, corpus fiscal, prompt de domínio e interface do produto |
| IIC | Produto de diagnóstico de incidentes de integração empresarial, com escopo multivendor |
| Core Python | SDK, orquestração, gateway LLM, infraestrutura RAG, evidências, autenticação e serviços compartilhados |
| Core UI | Cliente, sessão e componentes neutros compartilhados pelos shells dos produtos |

FISC e IIC são produtos distintos que reutilizam uma base comum. O FISC usa o
SDK público do core; não depende do pacote de produto IIC. A disponibilidade de conectores e canais no core não comprova sua validação
para cenários fiscais do FISC.

A implementação oficial está neste repositório, com core e core-ui consumidos
por releases do IIC. Consulte [a extração](EXTRACAO_CODIGO.md) para origem,
histórico e transição. Repositórios próprios não significam implantação,
homologação ou bancos compartilhados.

## 4. Escopo atual

| Dimensão | Recorte |
|---|---|
| Documento | NF-e, modelo 55, leiaute 4.00 |
| Contexto | Família, modelo, leiaute, ambiente, UF e eventos associados à chave de acesso |
| Entradas | Descrição do incidente, XML quando disponível e linha do tempo informada |
| XML | Parse seguro, chave e dígito verificador, retorno `cStat`, protocolo e validação XSD quando aplicável |
| Assinatura | Verificação de integridade XMLDSig no perfil implementado; confiança da cadeia do certificado não verificada |
| Correlação especializada | Duplicidade (`cStat 204`), divergência de chave (`cStat 539`) e timeout, conforme evidências e regras implementadas |
| Conhecimento | Recuperação de referências da base fiscal `dfe_kb`, quando configurada e disponível |
| Resultado | Fatos, hipóteses, evidências, lacunas e orientação de investigação |
| Interação | UI própria e API do produto; persistência de revisão e recursos compartilhados dependem da configuração |
| Ações fiscais | Somente leitura e análise de documentos e sistemas fiscais; nenhuma execução automática de ação fiscal |

O limite read-only se aplica aos documentos e sistemas fiscais. O FISC pode
persistir diagnósticos, revisões humanas e dados operacionais conforme a
configuração; isso não autoriza alteração de XML ou execução de ações fiscais.

Interpretar um código `cStat` ou recuperar uma referência não equivale a
possuir uma regra de diagnóstico especializada para toda rejeição.
Ausência de XML, fonte ou correlação suficiente deve aparecer como lacuna;
timeout isolado não comprova indisponibilidade da SEFAZ.

O contrato aceita todas as UFs e os valores `homologation` e `production`.
Essa aceitação é estrutural: não comprova cobertura normativa por UF,
vigência dos schemas em produção ou validação operacional nesses ambientes.

## 5. Casos de uso prioritários

1. **Investigar duplicidade:** ler o retorno 204 e verificar se a linha do
   tempo sustenta a hipótese de reenvio após timeout do mesmo documento.
2. **Investigar timeout:** explicitar o resultado desconhecido quando não há
   retorno e orientar a verificação autorizada antes de decidir por reenvio.
3. **Investigar divergência de chave:** organizar os achados do retorno 539
   conforme a correlação implementada, sem concluir além da evidência.
4. **Verificar o XML recebido:** apresentar resultados de chave, XSD,
   protocolo e assinatura, com limites e verificações não executadas.
5. **Apoiar revisão humana:** permitir que o responsável confronte hipótese,
   fontes e lacunas; confirmação de causa depende dessa revisão.

## 6. Fora do escopo atual

- Suporte completo a NFC-e, NFS-e, CT-e e MDF-e.
- Motor completo de cálculo tributário ou determinação de impostos.
- Cobertura normativa garantida por UF, regime e vigência.
- Consulta direta à SEFAZ ou integração fiscal SAP real homologada.
- Emissão, autorização, retransmissão, cancelamento, inutilização ou execução
  de contingência de documentos fiscais.
- Correção automática de XML ou escrita em sistemas fiscais.
- Validação completa de confiança ICP-Brasil, incluindo cadeia e revogação.
- Confirmação autônoma de causa pelo LLM ou substituição da decisão fiscal humana.

Novos documentos, conectores fiscais ou ações exigem definição de escopo,
contratos, fontes, testes e evidência de validação antes de serem anunciados.

## 7. Maturidade e limites de comunicação

Há implementação e artefatos locais de testes, UI, empacotamento e imagem.
Os aceites [P2](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/docs/ACEITE_P2.md) e [P6](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/docs/ACEITE_P6.md) registram verificações
locais históricas, incluindo testes com entradas sintéticas. Esses registros
não são uma nova execução nem confirmação do estado remoto do CI.
O [registro de pendências](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/docs/PENDENCIAS.md) distingue itens resolvidos de revisão
especializada e verificações ainda necessárias. Execução local, resultado de
benchmark e configuração aceita não constituem homologação fiscal ou prova
de operação contra SAP/SEFAZ reais.

Na apresentação pública, usar expressões como “apoia a investigação”,
“hipótese sustentada pelas evidências disponíveis” e “validação XSD quando
aplicável”. Evitar promessas de diagnóstico definitivo, cobertura fiscal
completa, integração homologada ou prontidão para produção sem evidência.

## 8. Texto-base para apresentação pública

> O Fiscal Incident Support Copilot (FISC) apoia equipes SAP AMS N2/N3 na
> investigação de incidentes de NF-e modelo 55, leiaute 4.00. Combina análise
> determinística de XML e eventos com recuperação de referências fiscais e
> explicação assistida por IA, distinguindo fatos, hipóteses e lacunas para
> revisão humana. É um produto com interface e domínio próprios que reutiliza
> o core compartilhado com o Integration Incident Copilot. O MVP é read-only,
> com avaliação baseada em casos sintéticos, sem homologação fiscal ou
> validação operacional em SAP/SEFAZ reais.

## 9. Fontes e manutenção

- [Decisão do nome](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/docs/DECISAO_NOME.md): marca e identificadores preservados.
- [Apresentação do produto](../README.md): problema, públicos e visão de produto.
- [Contrato fiscal](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/src/dfe_copilot/context.py): recorte aceito pelo runtime.
- [Plugin](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/src/dfe_copilot/plugin.py): ferramentas, correlação e base fiscal.
- [Decisões fiscais](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/docs/DECISOES.md): regras, limites e histórico de avaliação.
- [Pendências](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/docs/PENDENCIAS.md): restrições e validações externas em aberto.
- [Contratos do core](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/core/docs/CONTRACTS.md): fronteiras e compatibilidade.
- [Fronteiras de imports](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/architecture/boundaries.toml): dependências permitidas.

Este documento é a referência de posicionamento e escopo para o próximo
README. Detalhes operacionais permanecem nos manuais e contratos técnicos.
Mudanças de capacidade devem atualizar as fontes técnicas e esta síntese.
