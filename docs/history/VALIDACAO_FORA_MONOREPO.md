# Registro histórico — VALIDACAO_FORA_MONOREPO.md

> Snapshot anterior à organização documental de 2026-11-17. Não usar como
> instrução de instalação atual. Origem: [arquivo e commit](https://github.com/marcos-slima/fiscal-incident-support-copilot/blob/b34e8a6a89dabe8bd98e5b3bf919bc3baf2e4d9d/docs/VALIDACAO_FORA_MONOREPO.md).
> Links relativos foram fixados no snapshot de origem; comandos antigos são evidência histórica.

# Validação do FISC fora do monorepo

Data: 2026-11-16. Resultado: **build, testes fiscais, UI e execução em imagem
validados em um perfil externo**, com as adaptações descritas abaixo.
Esta evidência não é extração do repositório, release publicada ou homologação fiscal.

## Origem e isolamento

- Snapshot de implementação: commit
  [43d614476973e648c5dda253eac46c2bdb6bbc0f](https://github.com/marcos-slima/integration-incident-copilot/commit/43d614476973e648c5dda253eac46c2bdb6bbc0f).
- Bibliotecas obtidas do [CI aprovado de distribuição](https://github.com/marcos-slima/integration-incident-copilot/actions/runs/43956339134):
  `copilot-core 1.4.0` em wheel e `@copilot/core-ui 0.1.0` em tarball.
- Somente fontes do produto fiscal foram exportadas. Nenhuma fonte de core/IIC,
  `.venv` ou `node_modules` do monorepo foi copiada para o perfil.
- Dependências Python e npm foram resolvidas novamente em ambiente e caches
  próprios, usando os arquivos compartilhados verificados e registros de terceiros.
- Foram gerados `uv.lock` e `frontend/package-lock.json` externos.
- O wheel fiscal foi instalado antes dos testes. A execução usou `python -I`
  e `-o pythonpath=`, sem importar o produto a partir de `src`.
- Foi conferido que core e FISC vinham de `site-packages`, sem instalação
  editável, sem pacote IIC e sem caminho do monorepo em `sys.path`.

As bibliotecas foram distribuídas por artefato de CI, com hashes conferidos.
Não se afirma publicação em PyPI/npm, URL permanente de distribuição ou
reserva de nomes. O pacote local entregue preserva os artefatos utilizados.

## Resultados executados

| Verificação | Resultado |
|---|---|
| Resolução Python limpa | 176 pacotes instalados no ambiente inicial; core consumido por wheel |
| Torch CPU | `2.15.0+cpu`, sem pacotes NVIDIA no ambiente Python conferido |
| Suíte fiscal em Python 3.14.6 | **214 aprovados**, inclusive após as adaptações finais |
| Suíte fiscal em Python 3.12.14 | **214 aprovados** em contêiner, montando testes/dados/scripts/documentação, sem fontes de produto/core/IIC ou `.venv` local |
| Instalação JavaScript externa | Lock próprio; 116 pacotes adicionados, 117 auditados, sem vulnerabilidades reportadas pelo npm naquela execução |
| Frontend | Lint, typecheck e build aprovados; Node.js `26.13.1` |
| Wheel fiscal | `dfe-copilot 0.1.0` construído com UI obrigatória e instalado no ambiente externo |
| Imagem | Build com Python 3.12, uv `0.13.4`, dependências do lock externo e apenas wheels/manifests como entradas de aplicação |
| Execução | Usuário não root; core e produto instalados; sem fontes do IIC; suporte TLS do AMQP disponível |
| HTTP | Health, 401 sem sessão, login, cookie HttpOnly, catálogo fiscal, UI/assets, 422 de contexto inválido e logout aprovados |
| Ferramentas fiscais | Fixture sintética válida no XSD; caso 204 com eventos explícitos produziu `F-cStat`, `F-204` e hipótese `H1` |

O primeiro ambiente escolheu Python 3.14, permitido por `requires-python >=3.12`.
O perfil entregue fixa Python 3.12 como padrão; a versão 3.12 foi validada
separadamente no contêiner. A UI não requer Node no runtime Python: o bundle
compilado acompanha o wheel.

Imagem local: `fisc-standalone-validation:20261116`.

ID da imagem:
`sha256:f106d422cb2583f970d76697b80a576f9db60ab3b43ea04903c1852751eeeb58`.

Esse ID identifica uma imagem local; não é digest de imagem publicada em GHCR.

## Adaptações necessárias

Estas mudanças foram aplicadas ao perfil externo, **não aos manifests do monorepo**:

1. Fonte Python `workspace = true` substituída pelo caminho do wheel verificado.
2. `@copilot/core-ui` direcionado ao tarball verificado e hooks npm que chamavam
   o workspace removidos.
3. Torch declarado diretamente no consumidor e índice CPU configurado. Apenas
   declarar uma fonte uv para dependência transitiva não aplicou a escolha
   pretendida: a primeira tentativa começou a baixar CUDA e foi interrompida.
4. Dependências de teste declaradas localmente e Python 3.12 fixado no perfil.
5. Caminhos dos executáveis promptfoo ajustados à `.venv` da raiz externa,
   incluindo o gerador de splits. O provider deixou de inserir caminhos de
   fontes e diretórios ancestrais.
6. Instruções de build/execução adaptadas à raiz própria, preservando
   `dfe-copilot`, `dfe_copilot`, plugin `dfe` e `@copilot/dfe-ui`.

Nenhuma persona, digest de prompt, regra fiscal ou contrato foi alterado.
Os testes de digest e de consistência dos splits continuaram aprovados.
A execução real de promptfoo/LLM não foi realizada.

## Pacote reproduzível entregue

Arquivo local: `fisc-standalone-validation-20261116.zip` (2.775.713 bytes).

SHA-256:
`1ce323f5978ed0e38843b0bfb38b75cd44c252a30435c17fd77fa88c5a68098b`.

O pacote contém o perfil externo, fontes fiscais, bibliotecas compiladas,
wheel fiscal, locks, Dockerfile/contexto restrito, instruções, resultados
JUnit, evidências HTTP/recursos e inventário Python. Exclui `.venv`,
`node_modules`, `.env`, caches e fontes de core/IIC. `validation.json` e
`SHA256SUMS` permitem conferir a proveniência e integridade.
O ZIP é uma entrega local de validação, não um asset hospedado neste repositório.

O Dockerfile usa Python slim e instala as dependências nativas de
`python-qpid-proton`, incluindo `pkg-config` para conferir TLS. O contexto
Docker permite somente manifests, locks e wheels: não incorpora o checkout,
a UI fonte ou o ambiente virtual da máquina.

## Limites da evidência

- Testes fiscais usam dados sintéticos e controle/mocks de inferência.
- O smoke HTTP verifica execução, autenticação, assets e validação de contexto;
  as verificações fiscais positivas foram executadas diretamente dentro da imagem.
- Não houve inferência LLM real, ingestão ou uso de Qdrant externo, revisão
  persistente em PostgreSQL ou conexão a SAP/SEFAZ reais.
- Não foram executadas ações fiscais, migrações de dados reais ou deploy.
- A instalação externa resolve versões novas de terceiros; não reproduz o
  lock do monorepo. O lock externo registra a combinação efetivamente validada.
- Bibliotecas e FISC ainda não receberam publicação permanente em registro.
  Versões declaradas não são novas releases.

## Consequência para a evolução

A dependência do runtime FISC pode ser satisfeita por bibliotecas empacotadas,
sem checkout do IIC ou do core. A extração de código é tecnicamente viável
com os ajustes de manifests, hooks e caminhos acima. Permanecem decisões
separadas: integrar os PRs de preparação, publicar dependências de forma
permanente, escolher a governança e migrar o histórico/código do produto.

Consulte a [política de releases](https://github.com/marcos-slima/fiscal-incident-support-copilot/blob/b34e8a6a89dabe8bd98e5b3bf919bc3baf2e4d9d/docs/VERSIONAMENTO_RELEASES.md) e o
[mapa documental](https://github.com/marcos-slima/fiscal-incident-support-copilot/blob/b34e8a6a89dabe8bd98e5b3bf919bc3baf2e4d9d/docs/ORGANIZACAO_DOCUMENTACAO.md).
