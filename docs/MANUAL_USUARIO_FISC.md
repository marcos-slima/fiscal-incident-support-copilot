# Manual do usuário — FISC

## 1. Objetivo

O FISC ajuda a investigar incidentes de documentos fiscais eletrônicos usando
validações determinísticas, evidências e hipóteses explicativas. Ele não
substitui o responsável fiscal, não consulta a SEFAZ automaticamente no MVP e
não executa ações operacionais sobre o documento.

## 2. Acesso inicial

Abra a URL publicada pelo deployment, no Compose padrão `http://127.0.0.1:8002`.
O login web usa usuário e senha e cria um cookie de sessão `HttpOnly`. O usuário
deve ter sido configurado pelo administrador ou pelo bootstrap local documentado
no [guia de execução](DEPLOY.md).

Se o login falhar:

1. confirme a URL e a porta do FISC;
2. confirme que o usuário pertence ao deployment do FISC, não ao IIC;
3. peça ao administrador para verificar `WEB_UI_USERS`/cadastro persistente;
4. não copie `X-API-Key` para o formulário do navegador.

## 3. Solicitar um diagnóstico

Preencha:

1. **Descrição do incidente:** informe rejeição, timeout, erro de envio ou
   retorno observado.
2. **XML:** cole o XML original ou carregue um arquivo. Prefira `NFe`,
   `nfeProc`, `protNFe` ou retorno de lote completo; não cole somente um
   fragmento se o diagnóstico depender de XSD.
3. **Ambiente:** homologação ou produção.
4. **UF:** UF contextual do documento.
5. **Linha do tempo:** adicione envio, timeout, resposta ou erro com horário e
   chave de acesso, quando disponíveis.
6. Clique em **Diagnosticar**.

O formulário fiscal é derivado do schema publicado pelo plugin em
`GET /domain-plugins`. Se o plugin não aparecer, a UI e a API não estão usando
o runtime fiscal correto.

## 4. Como ler o resultado

### Fatos

Fatos são produzidos por ferramentas, parser, XSD, assinatura, chave,
protocolo, regras locais ou base fiscal. Exemplos:

- `F-cStat` — retorno encontrado no XML;
- `F-xsd` — resultado da validação XSD;
- `F-dv` — dígito verificador da chave;
- `F-sig` — resultado da verificação XMLDSig;
- `F-kb` — trecho recuperado da base fiscal.

### Hipóteses

Hipóteses são explicações propostas pelo modelo ou correlações ainda não
confirmadas. Uma hipótese não é autorização para reenviar, cancelar ou alterar
o documento.

### Lacunas

Lacunas como `G-xml`, `G-noxml`, `G-events`, `G-kb` e `G-sig` indicam que não
havia evidência suficiente. Uma lacuna reduz a confiança do diagnóstico.

### Confiança

- `model_confidence`: estimativa do modelo, limitada por guardrails;
- `diagnosis_confidence`: confiança calculada pelo pipeline com base nas
  evidências realmente disponíveis;
- `evidence_strength`: força objetiva das fontes.

Use `diagnosis_confidence` para decidir se é necessário escalar. Não use apenas
a confiança autorrelatada pelo modelo.

## 5. Revisão humana

Quando o resultado estiver pendente de revisão, o painel pode oferecer:

- aprovar;
- editar a causa proposta;
- rejeitar.

A retomada exige `CHECKPOINTING_ENABLED=true`, PostgreSQL e a chave de cifragem
descritos em `DEPLOY.md`. Sem persistência, o resultado pode informar revisão
necessária, mas não há retomada executável.

## 6. O que o FISC não faz

No escopo atual, o FISC não:

- envia XML para a SEFAZ;
- reenvia NF-e;
- cancela documento;
- inutiliza numeração;
- aciona contingência;
- altera o XML original;
- confirma autorização fiscal sem protocolo;
- substitui análise de especialista.

## 7. Tratamento de XML inválido

Um XML malformado pode resultar em diagnóstico com o fato `G-xml` ou outro
finding de recusa. Isso é diferente de erro HTTP: o serviço recebeu a entrada e
registrou que ela não pôde ser analisada com segurança.

XML bem-formado também pode falhar no XSD. Bem-formado não significa autorizado,
assinado, conforme ao schema ou fiscalmente correto.

## 8. Privacidade e segurança do usuário

- não cole senhas, certificados ou chaves privadas no XML;
- anonimize CNPJ, CPF, endereços e números quando o caso não exigir o valor real;
- confirme a política de soberania de dados antes de habilitar LLM cloud;
- use somente o deployment autorizado para documentos de produção;
- registre a evidência e o responsável pela decisão operacional fora do FISC,
  conforme o processo da empresa.
