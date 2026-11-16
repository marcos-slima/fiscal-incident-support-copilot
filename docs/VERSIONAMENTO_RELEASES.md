> Atualização de 2026-11-16 após a extração: código e próximas tags
> fisc/vX.Y.Z do FISC pertencem a este repositório. Core e core-ui permanecem
> no IIC, com releases core/v1.4.0 e core-ui/v0.1.0 já publicadas como assets.
> Os trechos abaixo sobre a fase documental/monorepo registram o plano anterior;
> a regra vigente de localização é esta e docs/EXTRACAO_CODIGO.md.

# Política de versionamento e releases

Definida em 2026-11-16 para a organização atual: código no monorepo IIC e
apresentação do FISC em repositório próprio. Esta política orienta as próximas
entregas; sua automação será implementada nas etapas de pipelines e distribuição.
Não cria tags, não altera manifests e não publica pacotes.

## 1. Unidades de versão independentes

| Unidade | Identificador | Fonte da versão | Estado declarado no checkout examinado |
|---|---|---|---|
| Produto IIC | `integration-incident-copilot` | `pyproject.toml` da raiz | `1.4.0` |
| Produto FISC | `dfe-copilot`, import `dfe_copilot` | `packages/dfe/pyproject.toml` | `0.1.0` |
| Biblioteca Python | `copilot-core` | `packages/core/pyproject.toml` | `1.4.0` |
| Biblioteca UI | `@copilot/core-ui` | `packages/core-ui/package.json` | `0.1.0`, `private: true` |

Versão declarada não comprova publicação em registro. Os números iguais de IIC
e core são circunstanciais: não há obrigação de evoluírem juntos.
Os shells privados de UI acompanham a entrega do respectivo produto; não
constituem uma quinta e sexta linha de releases públicas nesta política.
A divergência atual do shell IIC (`0.0.0`) deve ser reconciliada com a versão
do produto antes da próxima entrega que o empacote, sem publicar esse shell.

A documentação do FISC é rastreada por commit. Mudança exclusivamente editorial
não exige nova versão do produto. Documentação de uma entrega deve identificar
a versão e o commit de implementação a que se refere.

## 2. Histórico existente: não renumerar

Consulta ao GitHub em 2026-11-16 encontrou release IIC `v1.4.0`, publicada em
2026-10-20, e tags históricas incluindo `v2.0.0` e `v2.0.1`. O manifest da
`master` consultada ainda declara `1.4.0`. O FISC não tinha GitHub Releases.

Tags e releases são objetos distintos. Antes da próxima release IIC, investigar
os commits e a finalidade das tags 2.x, reconciliar manifest e histórico e
registrar a decisão. Não recriar, apagar ou mover tags históricas e não presumir
que `1.4.1` seja o próximo número apropriado. Esta política não resolve essa
pendência por renumeração automática.

## 3. Regra de incremento

Adotar `MAJOR.MINOR.PATCH` por unidade:

- **PATCH:** correção compatível, sem mudança intencional do contrato público.
- **MINOR:** capacidade adicional compatível com o contrato público.
- **MAJOR:** remoção, renomeação ou mudança incompatível de comportamento público,
  configuração, requisito operacional ou contrato; incluir plano de migração.

Para as unidades em `0.y.z`, adotar uma convenção explícita do projeto:
PATCH para correções compatíveis e MINOR para funcionalidades ou mudanças
incompatíveis, sempre destacando incompatibilidades nas notas. A passagem
para `1.0.0` exige estabilização dos contratos, instalação reproduzível e
validação do escopo anunciado. Não equivale a homologação fiscal.

Exemplos ilustrativos, não versões reservadas: correção fiscal compatível
`0.1.0 → 0.1.1`; nova capacidade fiscal `0.1.0 → 0.2.0`; mudança de contrato
público estável do core `1.x → 2.0.0`. A classificação considera o impacto
real: uma alteração em regra ou schema pode mudar o resultado do diagnóstico.

Para candidatas: tag `fisc/vX.Y.Z-rc.N`, versão Python `X.Y.ZrcN` e, para
pacotes npm, `X.Y.Z-rc.N`. A conversão deve ser explícita. Não usar o sufixo
SemVer literalmente no campo de versão Python sem normalização apropriada.

## 4. Tags, releases e local de publicação

Enquanto o código estiver no monorepo:

| Unidade | Tag nova no monorepo | Título de GitHub Release |
|---|---|---|
| IIC | `iic/vX.Y.Z` | IIC X.Y.Z |
| FISC | `fisc/vX.Y.Z` | FISC X.Y.Z |
| Core Python | `core/vX.Y.Z` | Copilot Core X.Y.Z |
| Core UI | `core-ui/vX.Y.Z` | Copilot Core UI X.Y.Z |

As tags antigas `v*` do IIC permanecem como histórico. A nova convenção começa
na próxima entrega aprovada. Cada tag aponta para o commit exato de build;
um commit pode receber tags diferentes, mas só as unidades alteradas ou
reempacotadas precisam de release. Tags e artefatos publicados são imutáveis.
Uma correção gera nova versão, nunca substituição silenciosa.

O GitHub Release técnico fica no repositório que contém o código marcado.
O repositório FISC mantém o índice com link para essa release. Não criar aqui
uma tag de software que marque apenas os arquivos de documentação: o arquivo
Source code gerado pelo GitHub conteria somente essa documentação.

Quando o código FISC migrar, tags futuras passam ao repositório FISC sem
reutilizar versões nem apagar o histórico no monorepo. A documentação registra
o limite da migração. Até lá, não é necessário duplicar GitHub Releases.

Não usar o marcador global “Latest” como versão de cada produto: o índice deve
apontar à release específica de FISC/IIC/core. Imagens de implantação usam
versão e digest, sem depender de `latest`.

## 5. Compatibilidade: pacote, contrato e conteúdo

| Superfície | Versão observada | Política |
|---|---|---|
| SDK Python | `1.0` | Major igual; minor suportado maior ou igual ao requerido |
| HTTP | `1.0` | Mesma negociação, com `X-Core-Contract-Version` |
| Plugin | `1.1` | Mesma negociação; o plugin fiscal requer `1.1` |
| Contexto fiscal | `schema_version="1"` | Mudança incompatível exige novo contrato e migração explícita |
| Prompt fiscal | `dfe-1.2.0` | Versão/digest próprios, separados da versão do produto |
| UI compartilhada | Pacote `0.1.0` | Compatibilidade validada com ambos os shells |

O runtime é a fonte da negociação de contratos. Corrigir o pacote sem mudar a
interface não exige incrementar o contrato. Elevar o pacote também não
concede compatibilidade automática a novos endpoints.

Preservar inicialmente os pins exatos de core e core-ui já declarados nos
produtos. Atualizar o pin é uma alteração explícita do consumidor, com testes
e changelog. O monorepo uv tem lock compartilhado; versões independentes não
eliminam essa coordenação. Um intervalo de versões só será adotado quando
houver testes que sustentem a faixa; não converter pins em intervalos nesta etapa.

A matriz de compatibilidade de cada release registra versões exatas, contratos,
commit de origem e evidência executada. A combinação hoje declarada é FISC
`0.1.0` + core `1.4.0` + core-ui `0.1.0`; ela é uma referência de implementação,
não uma release publicada ou certificação de toda a combinação em produção.

Prompts exigem avaliação/re-baseline conforme as regras do monorepo. Schemas,
manifestos normativos, corpus e configuração de modelos precisam de versão ou
hash no registro de entrega; mesma versão de software com outra configuração
LLM não constitui a mesma medição de comportamento.

## 6. Fluxo de uma entrega

1. Classificar a mudança e identificar as unidades afetadas.
2. Resolver pendências de versão, atualizar manifests, dependências, lockfiles
   e changelog da unidade, mantendo marca e identificadores técnicos.
3. Construir a partir de commit limpo e rastreável. Executar checks, quality
   gate e suíte exigidos pelo monorepo; para o FISC incluir testes fiscais,
   contratos, build da UI, wheels isolados e smoke de imagem. Mudanças de core
   ou core-ui exigem regressão de ambos os produtos; mudanças de prompt exigem
   medição correspondente. Teste não executado ou inconclusivo não conta como aprovado.
4. Registrar a matriz e as evidências, revisar incompatibilidades, recursos,
   migrações de dados, limitações e instruções de atualização/recuperação.
5. Publicar primeiro dependências novas exigidas pelo produto, depois os
   artefatos do produto. Enquanto não houver distribuição estabelecida,
   tratar o resultado como build/candidato, sem anunciar pacote instalável
   em registro. Uma release técnica pode anexar wheels e instruções explícitas.
6. Criar a tag e release correspondentes ao commit validado, anexar artefatos,
   checksums e notas. Promover os mesmos binários testados, sem rebuild silencioso.
7. Atualizar o índice do FISC, documentação e issue de origem com URLs e
   versões. Uma entrega fiscal não exige nova release do IIC quando ele não
   for alterado nem reempacotado.

Pre-release é marcada como tal no GitHub. Não promover candidata com falhas
ou lacunas obrigatórias de validação a entrega estável. Validações fiscais
externas ausentes permanecem explícitas, mesmo quando os testes técnicos passam.
Publicar release e implantar são ações distintas; a política não dispara deploy.

## 7. Evidência e artefatos mínimos

Cada entrega deve registrar:

- produto/unidade, versão, tag, repositório e commit completo;
- versões exatas de core, core-ui e contratos aplicáveis;
- checks executados, resultado, data e link do job ou relatório;
- wheels e/ou imagem conforme o canal oferecido; checksums e digest da imagem;
- versões/hashes de prompt, schemas, corpus e configuração/modelo usados na avaliação;
- requisitos de ambiente, migrações, incompatibilidades e limitações conhecidas;
- instruções de instalação, atualização e retorno à versão anterior.

Reverter imagem não reverte automaticamente banco ou índice RAG. Migrações
incompatíveis exigem estratégia própria de backup/restauração ou correção
progressiva documentada antes da entrega.

## 8. Changelogs, suporte e distribuição

Manter changelog por unidade junto ao código; notas devem selecionar alterações
daquela unidade, sem agregar indiscriminadamente todos os PRs do monorepo.
Mudança exclusivamente documental permanece no histórico deste repositório.
O [índice de releases](RELEASES.md) distingue o que existe do que está previsto.

Não há promessa de LTS ou manutenção de múltiplas linhas nesta etapa. A versão
suportada e exceções precisam ser declaradas por entrega. Um update do core
não altera instalações existentes: cada produto escolhe quando adotar a versão
e validar a combinação, inclusive para correções de segurança.

A definição de registro Python/npm, permissões e publicação de imagens pertence
à etapa de distribuição. Esta política não afirma que `copilot-core` ou
`@copilot/core-ui` já estejam disponíveis em registro público.

## 9. Referências

- [SemVer](https://semver.org/): significado de major, minor e patch e imutabilidade de versões.
- [Versões Python](https://packaging.python.org/en/latest/specifications/version-specifiers/): representação de pré-releases.
- [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases): vínculo entre releases, tags e arquivos de código-fonte.
- [Contratos do core](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/core/docs/CONTRACTS.md).
