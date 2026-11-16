# Como contribuir com o FISC

O FISC possui apresentação e documentação de produto neste repositório.
Sua implementação permanece no [monorepo IIC](https://github.com/marcos-slima/integration-incident-copilot), em `packages/dfe`.

## Escolha o canal

| Assunto | Onde abrir | Onde fica o PR |
|---|---|---|
| Dúvida de uso, problema ou proposta específica do FISC | [Issues do FISC](https://github.com/marcos-slima/fiscal-incident-support-copilot/issues/new/choose) | Neste repositório para documentação de produto; no monorepo para implementação |
| Identidade, escopo, README ou manual do FISC | Issue do FISC, quando precisar de discussão | Neste repositório |
| Código fiscal, testes, configuração, Docker ou CI do FISC | Issue do FISC | No monorepo |
| Falha do SDK, gateway, RAG ou core-ui compartilhado | [Issues do IIC/core](https://github.com/marcos-slima/integration-incident-copilot/issues) | No monorepo |
| Incidente específico do produto IIC | Issues do IIC/core | No monorepo |

Busque issues existentes antes de abrir uma nova. Para um erro simples de
texto, um PR direto é suficiente. Não é necessário abrir a mesma demanda nos
dois repositórios.

## Relatar problemas e propor mudanças

Use os templates de problema ou proposta. Informe o objetivo, versão/commit,
modo de execução, passos, comportamento esperado e resultado observado.
Use dados sintéticos ou anonimizados, sem XML real identificável, credenciais
ou chaves privadas. Descreva capacidades propostas como futuras, sem ampliar
o escopo anunciado antes da implementação e validação correspondentes.

## Alterações na documentação deste repositório

1. Crie um branch no seu fork ou no repositório, conforme sua permissão.
2. Edite o documento oficial indicado no [mapa documental](docs/ORGANIZACAO_DOCUMENTACAO.md).
3. Confira links, comandos, limites do MVP e renderização do Markdown/Mermaid.
4. Abra um PR com o problema, a mudança e as verificações realizadas.

O template de PR ajuda a registrar essas informações. A revisão e o merge
cabem ao mantenedor com permissão no repositório. Não há promessa de prazo de
resposta ou política de branches protegidas estabelecida por este documento.

## Alterações de código no monorepo

1. Registre o problema específico do FISC aqui.
2. Leia o [AGENTS.md](https://github.com/marcos-slima/integration-incident-copilot/blob/feat/dfe-runtime-existing-kb/AGENTS.md), os contratos e as decisões aplicáveis no monorepo.
3. Implemente e teste no monorepo, usando uv e preservando as fronteiras entre produtos e core.
4. Execute os checks exigidos pelo monorepo, incluindo o quality gate antes do commit.
5. Abra o PR no monorepo com link completo para a issue do FISC e descreva os impactos em FISC, IIC e core.
6. Publique o link do PR na issue original. Depois do merge, registre a versão
   ou commit que contém a correção e encerre a issue após conferir o resultado.

Não use `Fixes #N` no PR do monorepo para se referir a uma issue do FISC:
`#N` aponta para a numeração do próprio monorepo. Use a URL completa; não
presuma encerramento automático entre repositórios.

Se a triagem mostrar que a falha é compartilhada, mantenha a discussão técnica
na issue do core e vincule a ocorrência fiscal. Evite dois acompanhamentos
independentes para a mesma correção.

## Critérios de revisão

- Escopo atual: NF-e 55, leiaute 4.00, análise read-only de documentos/sistemas fiscais.
- Fatos, hipóteses e lacunas continuam distinguíveis; causa não é confirmada pelo LLM.
- Identificadores `dfe-copilot` e `dfe_copilot` permanecem preservados.
- Mudanças de prompt, contratos, schemas e regras seguem os requisitos específicos do monorepo.
- Documentação informa o que foi implementado e o que foi efetivamente validado.
