# Modelo de notas de release

Modelo para preenchimento; não representa uma entrega publicada.

## Identificação

- Unidade e versão:
- Status: candidata / estável técnica (não significa homologação fiscal)
- Repositório, tag e commit completo:
- Data de publicação:
- Versão de documentação/commit:

## Problema e comportamento entregue

Descrever o gatilho, o comportamento anterior e o novo resultado.

## Componentes e compatibilidade

| Componente | Versão/hash exato | Evidência |
|---|---|---|
| Core Python | A preencher | A preencher |
| Core UI | A preencher | A preencher |
| Operações / combinação de core / revisão de schema | A preencher | A preencher |
| SDK / HTTP / plugin / contexto fiscal | A preencher | A preencher |
| Prompt / schemas / corpus | A preencher | A preencher |
| Modelo, origem e configuração usados na avaliação | A preencher | A preencher |

Para unidade que não utiliza uma superfície, declarar “não aplicável” e justificar.
Não converter exemplos em evidência de teste.

## Artefatos

Informar URL, SHA-256 dos arquivos, digest OCI quando houver e proveniência do build.

## Verificações

Registrar comando/job, data, resultado e link. Distinguir testes sintéticos,
execução local, CI remoto e validação externa. Identificar falhas ou checks
não executados e bloquear a promoção quando forem obrigatórios.

## Atualização, migrações e recuperação

Indicar pré-requisitos, dependências publicadas, alteração de configuração,
migração de dados e procedimento de retorno ou recuperação.

## Limitações e pendências

Explicitar escopo fiscal e evidência externa ausente. Referenciar issues/PRs
por URL completa. Não prometer capacidades sem validação correspondente.
