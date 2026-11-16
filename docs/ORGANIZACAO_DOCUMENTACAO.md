# Organização da documentação e dos canais

Estado: organização inicial de 2026-11-16, durante a permanência do código no monorepo.

## Fontes oficiais

| Conteúdo | Fonte oficial | Responsabilidade de manutenção |
|---|---|---|
| Apresentação pública | [README do FISC](../README.md) | Mantenedor do produto |
| Identidade, público e escopo | [Identidade e escopo](IDENTIDADE_ESCOPO_FISC.md) | Responsável pelo produto; revisão fiscal quando necessária |
| Operação pela interface e interpretação dos resultados | [Manual do usuário](MANUAL_USUARIO_FISC.md) | Mantenedor do produto, em conjunto com mudanças da UI |
| Navegação | [Índice documental](README.md) | Mantenedor do produto |
| Canais e fluxo de contribuição | [CONTRIBUTING](../CONTRIBUTING.md) | Mantenedor dos repositórios |
| Código e testes fiscais | [`packages/dfe`](https://github.com/marcos-slima/integration-incident-copilot/tree/feat/dfe-runtime-existing-kb/packages/dfe) | Mantenedor da implementação fiscal |
| Instalação, ambientes, Docker e CI | [DEPLOY.md](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/docs/DEPLOY.md) e workflows do monorepo | Mantenedor da implementação |
| Decisões e regras fiscais | [DECISOES.md](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/docs/DECISOES.md) | Mantenedor fiscal, com revisão especializada quando aplicável |
| Contratos públicos e compatibilidade | [Contratos do core](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/core/docs/CONTRACTS.md) | Mantenedor do core |
| Limitações e evidências técnicas | [PENDENCIAS.md](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/packages/dfe/docs/PENDENCIAS.md), aceites e testes no monorepo | Responsável pela verificação |

As responsabilidades são funções de manutenção, não novos cargos ou
aprovações atribuídos a pessoas. Permissões de acesso não foram alteradas.

A [política de versionamento](VERSIONAMENTO_RELEASES.md) define unidades,
compatibilidade e entrega; o [índice de releases](RELEASES.md) acompanha
as publicações efetivas. Os changelogs técnicos ficam junto ao código.

A [validação fora do monorepo](VALIDACAO_FORA_MONOREPO.md) registra o perfil
externo, adaptações e evidência local, sem substituir os contratos técnicos.

## Evitar duplicação

Este repositório é a referência editorial dos documentos de produto acima.
As cópias anteriores no monorepo são históricas ou transitórias: atualizações
editoriais devem ocorrer aqui. Na próxima atualização desses documentos no
monorepo, substituir cópias por links para o documento oficial, preservando
os registros técnicos e históricos.

Os arquivos locais usados na preparação são cópias de trabalho. Depois da
publicação, o estado da branch `main` deste repositório é a referência pública;
confira-o antes de reaplicar uma cópia local.

O README técnico de `packages/dfe` permanece útil para desenvolvimento. Sua
síntese de escopo deve apontar ao documento de produto, sem evoluir como uma
segunda especificação. Em divergências sobre comportamento, verifique código,
contratos e evidência; corrija a descrição do produto sem ampliar promessas.

## Quando uma mudança atravessa repositórios

Uma mudança de comportamento começa no monorepo com seus testes e contratos.
Se alterar instruções de uso, capacidades ou limites, prepare também o PR
correspondente neste repositório, com links recíprocos. Publique a documentação
da capacidade quando a implementação estiver disponível e identifique a
versão/commit de referência. Propostas ainda não entregues devem ser marcadas
como propostas.

Os links técnicos atuais usam a branch `feat/dfe-runtime-existing-kb`.
Quando houver release ou integração na branch principal, revisar os links e
preferir tags/commits para evidências históricas. Mudança de URL deve incluir
verificação dos destinos e atualização deste índice.

## Demanda, implementação e encerramento

A issue do FISC acompanha o efeito para o usuário. O PR do monorepo acompanha
a implementação. Vincule ambos; registre o commit/versão entregue antes de
encerrar o acompanhamento. Demandas compartilhadas com IIC/core são tratadas
no monorepo, com referência à ocorrência fiscal.

Consulte o [guia de contribuição](../CONTRIBUTING.md) para escolher o canal.
Esta etapa não migra código, histórico, issues antigas ou pipelines e não
estabelece calendário de releases.
