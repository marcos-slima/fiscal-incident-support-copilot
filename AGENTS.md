# FISC — instruções para agentes

Produto fiscal independente sobre copilot-core e @copilot/core-ui.
Código em src/dfe_copilot, frontend em frontend, testes em tests.

- Usar uv; não instalar dependências Python com pip/poetry diretamente.
- Preservar identificadores dfe-copilot, dfe_copilot, dfe e @copilot/dfe-ui.
- Produtos importam o core somente por app.sdk; não copiar core nem importar IIC.
- Escopo NF-e 55/leiaute 4.00, read-only fiscal, revisão humana.
- Não alterar prompts/digests sem avaliação e re-baseline reais.
- Fatos determinísticos não são hipóteses LLM; timeout não prova indisponibilidade.
- Manter parse XML sem rede, hashes normativos e fail-closed nos contratos.
- Bibliotecas têm versões e hashes em shared-libraries.json; atualizar locks explicitamente.
- Ler docs/DEPLOY.md e .github/workflows/ci.yml para comandos. Testes CI usam
  wheel instalado: python -I -m pytest -c pyproject.toml -o pythonpath= tests.
- Não declarar homologação, SAP/SEFAZ real ou inferência real sem evidência.
- Arquivos de revisão e datasets sintéticos são versionados; .env/caches não.

- Fonte canônica de core/UI/operações: marcos-slima/copilot-platform; cada componente tem versão própria.
