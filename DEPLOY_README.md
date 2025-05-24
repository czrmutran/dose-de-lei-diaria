# Guia rápido de deploy – Flask

Última geração: 2025-05-12T21:30:28.852716 UTC

## Passos resumidos

1. **Suba este diretório para um repositório Git** (GitHub, GitLab, Bitbucket).
2. **Crie um serviço Web** no Render *ou* Railway apontando para o repositório.
   * Build Command: `pip install -r requirements.txt`
   * Start Command: `gunicorn src.main:app`
3. Configure variáveis de ambiente:
   * `FLASK_ENV=production`
   * `SECRET_KEY=<string‑secreta>`
   * *(opcional)* `DATABASE_URL` se for usar Postgres
4. Aponte seu domínio com registros DNS conforme instruções do provedor (CNAME/A).
5. Pronto! O app roda em HTTPS e replica exatamente o site original.

Para detalhes completos, consulte o README original ou o manual do provedor.
