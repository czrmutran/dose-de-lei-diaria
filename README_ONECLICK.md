# Deploy automático (1‑Click) – Render

Clique no botão abaixo **depois** de publicar este repositório no GitHub:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

O Render lerá `render.yaml` e criará:
* Um serviço **Web (Free Plan)** usando Python/Flask.
* Um banco **PostgreSQL (Free Plan)**, gerando a variável `DATABASE_URL`.
* Variáveis `SECRET_KEY` e `FLASK_ENV`.

Após aceitar, o deploy começa automaticamente e seu app fica em HTTPS.
