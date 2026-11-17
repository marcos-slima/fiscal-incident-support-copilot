# Avaliação de um repositório neutro para a plataforma

Data: 2026-11-17. Estado: recomendação arquitetural e critérios de evolução;
nenhum repositório de plataforma foi criado e nenhuma biblioteca foi movida
nesta etapa. A avaliação não registra uma DA implementada no core.

## 1. Recomendação

Adotar **um único repositório neutro para core Python, core-ui e recursos
operacionais compartilhados** como destino arquitetural. Nome de trabalho:
**copilot-platform**, ainda não reservado nem criado.

Executar a mudança depois de consolidar o IIC como consumidor dos artefatos
e tornar os testes, gates e builds compartilhados independentes da raiz do
repositório IIC. A prioridade imediata é essa consolidação, pois o FISC já
possui identidade, código, CI e consumo de bibliotecas independentes.

O terceiro repositório melhora a governança da base comum. O benefício técnico
não depende de uma organização GitHub nova, de renomear pacotes ou de converter
o core em serviço remoto.

## 2. Situação verificada

| Aspecto | Evidência em 2026-11-17 | Consequência |
|---|---|---|
| FISC independente | main em 656f6ce85e4067989e1c93b7dc0eea87d27636b3; extração preservou 25 commits fiscais | A autonomia do produto já está atendida |
| Consumo compartilhado | shared-libraries.json fixa wheel, tarball UI e operações por URL e SHA-256 | O FISC pode trocar de origem em um upgrade explícito |
| Distribuição permanente | Releases core/v1.4.0 e core-ui/v0.1.0 no IIC | Não há urgência de mudar o local para tornar os pacotes consumíveis |
| Consolidação do IIC | PRs 24, 25 e 26 continuam abertos; master declara IIC 1.4.0, sem dependência explícita de copilot-core e sem packages/core | A separação preparada não está consolidada na branch principal do IIC |
| Contratos públicos | SDK/HTTP 1.0, plugin 1.1 e core-ui 0.1.0 | Há fronteiras que permitem migrar sem renomear a API |
| Ferramentas do core | Gates usam CLAUDE.md, data/eval, data/sample_docs e caminhos packages/core na raiz | Copiar apenas packages/core não move a capacidade de validar a plataforma |
| Recursos operacionais | Builder reúne Alembic, dashboards e validador que hoje ficam fora de packages/core | Operação precisa de responsabilidade e histórico próprios no corte |
| Conteúdo do core | Regras SAP/integração, supervisão SAP/SaaS/genérica e skills multivendor fazem parte do pacote | Neutralidade de repositório não comprova neutralidade de domínio |

As evidências de runtime/testes são as já registradas na validação e extração.
Esta etapa inspecionou código, manifests, releases e estado remoto dos PRs;
não repetiu execução de serviços, testes fiscais ou homologação.

## 3. Comparação das opções

| Estrutura | Benefício | Limitação/custo | Parecer |
|---|---|---|---|
| Core e UI continuam no IIC | Menor operação; URLs e builds existentes preservados | Propriedade e apresentação da plataforma continuam associadas ao IIC | Adequada durante a consolidação |
| Um repositório de plataforma com Python, UI e operações | Identidade neutra, contratos e releases com governança própria; mudanças compartilhadas coordenadas | Migração de testes/dados/decisões/CI e um repositório adicional para manter | Destino recomendado |
| Repositórios separados para backend e UI | Permissões e manutenção muito independentes | Mais coordenação e pipelines para apenas dois produtos consumidores | Sem benefício demonstrado agora |
| Espelho ou cópia do core em cada produto | Acesso imediato às fontes | Divergência, correções duplicadas e incerteza sobre a fonte oficial | Inadequada como distribuição |
| Core central como serviço HTTP obrigatório | Operação centralizada em outro modelo | Altera latência, disponibilidade, soberania e contrato de plugins; deixa de ser apenas organização GitHub | Decisão arquitetural separada |

Manter Python e UI no mesmo repositório de plataforma não exige igualar suas
versões. Um workspace uv compartilha lockfile entre seus membros; IIC e FISC,
como consumidores externos, devem continuar com locks próprios.

## 4. Fronteiras propostas

| Local | Responsabilidade |
|---|---|
| copilot-platform | SDK/core, gateway, orquestração comum, mecanismos de evidência, infraestrutura RAG, autenticação comum e contratos |
| copilot-platform | Core-ui, suas interfaces públicas, tipos, estilos e testes de componentes |
| copilot-platform | Cadeia de migrations do core, bundle operacional, contrato de configuração e scripts compartilhados |
| copilot-platform | Testes de contrato, testes do core, baselines e dados de avaliação realmente compartilhados, documentação e decisões da plataforma |
| IIC | Shell/UI, configuração, documentação, cenários e entrega do produto de integração |
| FISC | Plugin, ferramentas, regras e corpus fiscais, shell/UI, testes e entrega fiscal |

Esta é uma classificação a confirmar por inventário de arquivos. O core atual
contém mecanismos e conteúdo de integração. Regras e conectores úteis a vários
consumidores podem permanecer como capacidades compartilhadas documentadas.
Itens exclusivos de produto precisam de decisão explícita sobre seu dono.
Não retirar regras ou mudar roteamento durante uma simples mudança de repositório.
Uma modularização de domínio pode exigir DA, testes e medição próprios.

## 5. Governança necessária

- Um responsável pela manutenção da plataforma, com critérios de aceitação de
  mudanças compartilhadas. É uma função proposta, não atribuição de pessoa ou permissão.
- Issues da plataforma para bugs de SDK/core/core-ui; issues de produto mantêm
  o efeito para o usuário e referenciam a correção compartilhada.
- Versionamento independente de core e core-ui; operações seguem a versão do core.
- Compatibilidade por contrato e combinação testada, com deprecações e migrações
  explícitas. Nenhum produto atualiza sua instalação apenas porque o core publicou.
- CI da plataforma valida os contratos e consumidores IIC/FISC em commits
  identificados. CI de cada produto continua validando sua versão instalada.
- Releases próprias e um fluxo claro para correções de segurança e versões
  suportadas, sem prometer LTS ou múltiplas linhas antes de haver manutenção definida.

Os nomes copilot-core, app.sdk e @copilot/core-ui permanecem. Nome de repositório
não concede controle de scope npm. A distribuição por assets pode continuar,
com evolução de registros tratada separadamente.

## 6. Critérios para autorizar o corte técnico

| Critério | Situação atual | Evidência de saída necessária |
|---|---|---|
| FISC instala bibliotecas sem checkout do core | Atendido na validação anterior | Preservar os testes e smoke no novo canal |
| IIC consolidado como consumidor | Pendente | Branch principal construída/testada com artefatos externos |
| PRs de preparação reconciliados | Pendente | Rever 24–26 para não reintroduzir o FISC como produto ativo no IIC |
| Testes, gates e dados têm dono e localização | Pendente | Inventário com cobertura preservada e referências atualizadas |
| Core/UI/operação constroem isoladamente | Parcial: artefatos e smoke já verificados | Build e suíte completos da plataforma sem estrutura IIC |
| Responsabilidade e processo de release definidos | Proposta nesta avaliação | Regras de contribuição, suporte e publicação registradas |
| Compatibilidade dos dois produtos comprovada | FISC comprovado; IIC principal pendente | Mesmo candidato exercitado por ambos em versões/commits identificados |
| Continuidade das URLs existentes preservada | Releases atuais disponíveis | Assets antigos mantidos e novo canal validado antes do upgrade |

Conclusão do quadro: a criação imediata não resolve a pendência principal do
IIC e acrescenta coordenação durante a transição. Há base para preparar o
inventário; a execução do corte depende dos critérios pendentes.

## 7. Plano de evolução condicionado

1. **Consolidar o IIC.** Revisar/rebasear os PRs 24–26 considerando o FISC já
   extraído. Retirar dependências de workspace e pipelines que tratam o FISC
   histórico como fonte ativa. Validar o produto IIC com bibliotecas publicadas.
2. **Inventariar a plataforma.** Classificar core, UI, testes, fixtures,
   baselines, skills, contratos, Alembic, dashboards, scripts e decisões.
   Separar mecanismo compartilhado de configuração e dados de cada produto.
3. **Desacoplar a validação.** Remover pressupostos sobre a raiz IIC dos
   builders/gates. Conferir COPILOT_HOME, descoberta de recursos, estrutura de
   distribuição e cadeia de migrations, sem mudar IDs ou regras fiscais.
4. **Criar o repositório neutro após a decisão de execução.** Preservar o
   histórico relevante de cada caminho e registrar o corte. Migrar core, UI e
   operação juntos, com versões de componentes independentes.
5. **Publicar um candidato e validar ambos os produtos.** Usar o mesmo binário
   testado, contratos explícitos e matriz de versões; comparar resultados e
   digests. Mudança de prompt exige re-baseline real, não simples regravação.
6. **Publicar a primeira entrega pelo novo canal.** Escolher nova versão pelo
   impacto da mudança. Não reiniciar a numeração nem substituir bytes de uma
   versão já publicada. Preservar os assets e tags antigos no IIC.
7. **Atualizar consumidores separadamente.** Alterar URLs, hashes e locks do
   FISC e IIC em PRs próprios. Validar instalação, UI, imagem e operação antes
   de desativar o publicador antigo. Registrar um upgrade completo de cada produto.
8. **Encerrar a transição.** Marcar as fontes antigas como históricas,
   documentar suporte e responsáveis e manter links de proveniência. Não
   apagar releases antigas necessárias a instalações e builds reproduzíveis.

O início do novo publicador e a parada do antigo devem ter um corte explícito:
uma única fonte de evolução do core. A migração não cria um segundo fork ativo.
As URLs atuais de assets não passam a apontar automaticamente ao novo repositório;
os consumidores permanecem fixados nelas até uma atualização explícita.

## 8. Benefícios, impactos e limites

**FISC:** ganha um fornecedor de plataforma com identidade própria e canal de
bugs compartilhados. O custo de adoção é atualizar origem, hashes/locks e
validar a combinação; seu domínio e a independência de release permanecem.

**IIC:** passa a apresentar claramente o produto e a consumir a mesma plataforma
que o FISC. Precisa concluir a separação que hoje está nas branches de
preparação; deixa de ser também o local de evolução da biblioteca.

**Plataforma:** ganha backlog, testes, contratos e publicação próprios. Assume
o custo permanente de manter regressão de consumidores, dependências,
recursos operacionais e compatibilidade. Repositório neutro não é evidência
de maior maturidade fiscal nem certificação de ambientes externos.

Não há evidência de equipes separadas, terceiro consumidor ou volume de releases
que exija quatro repositórios. Se esses requisitos surgirem, a organização de
UI e backend pode ser reavaliada. A presente recomendação se baseia nos dois
produtos e nos acoplamentos efetivamente observados.

## 9. Fontes verificadas

- [Extração FISC](EXTRACAO_CODIGO.md) e [validação externa](VALIDACAO_FORA_MONOREPO.md).
- [Dependências FISC](../shared-libraries.json).
- [PR 24](https://github.com/marcos-slima/integration-incident-copilot/pull/24),
  [PR 25](https://github.com/marcos-slima/integration-incident-copilot/pull/25) e
  [PR 26](https://github.com/marcos-slima/integration-incident-copilot/pull/26).
- [Manifest IIC principal](https://github.com/marcos-slima/integration-incident-copilot/blob/master/pyproject.toml).
- [Contratos do core](https://github.com/marcos-slima/integration-incident-copilot/blob/43d614476973e648c5dda253eac46c2bdb6bbc0f/packages/core/docs/CONTRACTS.md).
- [Gates e pressupostos de diretório](https://github.com/marcos-slima/integration-incident-copilot/blob/43d614476973e648c5dda253eac46c2bdb6bbc0f/packages/core/src/app/evaluation/gates.py),
  [descoberta da raiz](https://github.com/marcos-slima/integration-incident-copilot/blob/43d614476973e648c5dda253eac46c2bdb6bbc0f/packages/core/src/app/paths.py),
  [builder operacional](https://github.com/marcos-slima/integration-incident-copilot/blob/43d614476973e648c5dda253eac46c2bdb6bbc0f/scripts/build_shared_distribution.py) e
  [regras compartilhadas](https://github.com/marcos-slima/integration-incident-copilot/blob/43d614476973e648c5dda253eac46c2bdb6bbc0f/packages/core/src/app/agent/rules.py).
- [uv workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces/): membros e lock compartilhado.
- [Workflows reutilizáveis](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows): opção de padronização de CI entre repositórios; não configurada nesta avaliação.
