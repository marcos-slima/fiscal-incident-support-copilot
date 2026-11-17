# Versionamento e releases do FISC

| Unidade | Fonte da versão | Valor atual | Local de release |
|---|---|---|---|
| Produto dfe-copilot | pyproject.toml deste repositório | 0.1.0 declarado | FISC, tag fisc/vX.Y.Z |
| UI @copilot/dfe-ui | frontend/package.json | 0.1.0 | acompanha entrega FISC |
| copilot-core | plataforma packages/core/pyproject.toml | 1.4.1 adotado | plataforma, core/vX.Y.Z |
| @copilot/core-ui | plataforma packages/core-ui/package.json | 0.1.1 adotado | plataforma, core-ui/vX.Y.Z |
| copilot-operations | plataforma operations/component.toml | 1.0.0 adotado | plataforma, operations/vX.Y.Z |

Cada componente evolui independentemente. Adotar uma biblioteca não publica
release de produto automaticamente; documentação editorial não exige nova
versão de software. Os identificadores dfe-copilot/dfe_copilot são preservados.

## Atualizar dependências

Atualize URL/versão e SHA-256 em shared-libraries.json, a fonte em pyproject.toml,
o pacote UI em frontend/package.json e ambos os locks. Execute as validações
[do deploy](DEPLOY.md) e a CI própria: UI, wheel instalado, testes, Compose e imagem.
Revise compatibilidade do SDK/plugin e a combinação de operações/core testada.
Não copie código do core para o FISC. Não aplicar migrations durante build.

## Publicar o produto

Preparar release por PR com escopo, versão e commit exatos, evidência de testes,
limitações, dependências e instruções de atualização. Use o [modelo](MODELO_NOTAS_RELEASE.md).
A CI atual valida e armazena wheel de candidato; não é publicação automática de
release, imagem GHCR ou pacote em registro. Configuração desses canais exige
mudança explícita e verificação do destino.

Após aprovar a entrega, criar a tag/release fisc/vX.Y.Z neste repositório e
atualizar [o índice](RELEASES.md) com link, commit e versões compartilhadas.
Não sobrescrever assets nem mover tags publicadas. Incompatibilidade exige
plano de migração; seguir SemVer para versões estáveis e explicitar a política 0.y.z.
Não converter aprovação editorial em homologação fiscal.

## Histórico

Releases antigas core/v1.4.0 e core-ui/v0.1.0 continuam no IIC para reproduzir
builds anteriores. Não criar novas releases FISC no IIC. A política do antigo
monorepo está [arquivada](history/before-reorganization/docs/VERSIONAMENTO_RELEASES.md).
[Adoção atual](ADOCAO_PLATAFORMA.md) · [política da plataforma](https://github.com/marcos-slima/copilot-platform/blob/main/docs/RELEASES.md).
