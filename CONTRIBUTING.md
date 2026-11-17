# Como contribuir

O código e a documentação de produto do FISC são mantidos neste repositório.
Abra aqui issues e PRs sobre comportamento fiscal, frontend, testes, execução,
CI, identidade ou documentação. Evite duplicar a mesma demanda.

Problemas compartilhados de SDK, gateway, RAG ou core-ui vão para o
[Copilot Platform](https://github.com/marcos-slima/copilot-platform/issues).
Vincule as ocorrências com URLs completas. Correções de core são adotadas
aqui por atualização explícita das dependências, locks e hashes.

## Desenvolvimento

Use uv para dependências Python, nunca pip/poetry diretamente. Leia AGENTS.md,
instale os artefatos versionados e execute os comandos de docs/DEPLOY.md.
Preserve dfe-copilot, dfe_copilot e os contratos do SDK/plugin.

Antes do PR, execute lint, testes fiscais contra o wheel instalado, build da
UI e build/smoke da imagem conforme .github/workflows/ci.yml. Mudança de prompt
exige medição e baseline reais; não regrave o digest apenas para passar testes.
Dados de demonstração devem ser sintéticos/anonimizados. Não publique segredos.

## Revisão e entrega

O PR descreve o problema, comportamento final, evidência executada e limitações.
Mudança de escopo, schema ou regra deve atualizar documentação e casos de
regressão. Uma release FISC usa tag fisc/vX.Y.Z neste repositório, com os
artefatos do commit validado; a extração de código não cria release de produto.

A suíte do core e seus quality gates continuam no IIC. Este repositório
verifica o produto consumidor; não mantém uma cópia da implementação do core.
