# Pendências e limites atuais do FISC

A separação do produto e da plataforma foi concluída. Backend, UI, CI e imagem
são independentes; não registrar sua extração como trabalho futuro.

| Item | Estado e próximo passo |
|---|---|
| Revisão fiscal especializada (P11 histórico) | Continua necessária; aprovação anterior por responsável do produto não equivale a revisão de especialista fiscal |
| SAP/SEFAZ e operação real | Fora da evidência desta migração; requer validação explícita e escopo autorizado |
| Inferência/modelos e KB no deployment | Provisionar e medir no ambiente alvo; testes de wheel/UI/imagem não comprovam inferência real |
| Release pública do produto | Manifest 0.1.0 não é release; preparar entrega segundo a política e registrar no índice |
| Migrations em ambiente persistente | Aplicação explícita pelo operador, após backup, destino e compatibilidade confirmados |

## Itens de estrutura resolvidos

FISC tem fonte fiscal em src/dfe_copilot e UI em frontend. Consome core 1.4.1,
core-ui 0.1.1 e operações 1.0.0 da plataforma. Os 214 testes, UI, wheel instalado
e smoke da imagem passaram na adoção. A antiga pendência P10 de testes do core
no ambiente de preparação foi sucedida pela suíte/infraestrutura da plataforma;
isso não comprova os testes operacionais externos acima.

Resultados anteriores de ingestão, dataset, assinatura e prompts mantêm o alcance
registrado em [decisões](DECISOES.md) e [histórico](history/README.md). Não foram
remedidos ou certificados por esta atualização editorial.
[Arquitetura](ARCHITECTURE.md) · [releases](RELEASES.md) · [deploy](DEPLOY.md).
