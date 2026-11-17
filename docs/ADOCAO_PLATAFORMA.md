# Adoção de Copilot Platform

A decisão de 2026-11-17 é manter core Python, core-ui e operações num único
repositório neutro, copilot-platform, com versões independentes.

| Dependência | Versão adotada | Canal |
|---|---|---|
| copilot-core | 1.4.1 | wheel GitHub Release core/v1.4.1 |
| @copilot/core-ui | 0.1.1 | tarball GitHub Release core-ui/v0.1.1 |
| copilot-operations | 1.0.1 | bundle GitHub Release operations/v1.0.1 |

URLs e SHA-256 estão em shared-libraries.json; locks Python/npm são atualizados
explicitamente. As releases antigas do IIC continuam disponíveis para reproduzir
builds anteriores. O FISC não copia implementação da plataforma nem depende do
checkout do IIC. app.sdk e os identificadores dfe-copilot/dfe_copilot são preservados.
A versão FISC permanece 0.1.0; adotar uma biblioteca não publica automaticamente
a release do produto. Cada componente aplica seu próprio versionamento.

A plataforma executa seus testes, migrations/dashboards e compatibilidade com
commits fixados dos produtos. O FISC executa seus 214 testes, wheel, UI e imagem
em seu pipeline próprio. A combinação de operações é testada com core 1.4.1;
esta adoção não aplica migrations nem muda revisões já publicadas.

Documentos de extração/aceite anteriores são históricos. A avaliação da etapa 11
foi sucedida por esta decisão; novas mudanças compartilhadas pertencem à plataforma.
Escopo fiscal, prompts e hashes normativos não foram alterados. Testes locais/CI
não representam homologação SAP/SEFAZ, execução LLM real ou deploy de produção.
