# Attribute Procedurals — Django + Supabase

Premium corporate website for **Attribute Procedurals**, with Django as the backend and **Supabase PostgreSQL** as the production database.

## Stack
- Django 5.2+
- Supabase PostgreSQL
- psycopg 3
- `dj-database-url`
- Django Templates
- Django Admin
- CSRF-protected contact form
- Environment variables via `python-dotenv`

## Database architecture

```text
Website
   |
   v
Django
   |
   +---- Django Admin
   |
   +---- Supabase PostgreSQL
   |
   +---- Email provider
```

Supabase is used as the managed PostgreSQL database. Django remains responsible for application logic, validation, forms, admin and migrations.

## Local setup

### Windows PowerShell
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Linux/macOS
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

If `DATABASE_URL` is present, Django connects to Supabase. If it is absent, development falls back to SQLite.

## Supabase setup

1. Create a Supabase project.
2. Open **Connect** and copy a PostgreSQL connection string.
3. Put it in `.env` as `DATABASE_URL`.
4. Run `python manage.py migrate`.
5. Create your Django admin account.

Do not commit `.env` or database credentials.

See `supabase/README.md` and `supabase/schema.sql` for the database reference.

## Main database entities

- `ContactMessage` — website enquiries
- `Project` — portfolio projects
- `ResearchProject` — research and R&D work
- `Insight` — articles/insights
- `Technology` — technology stack
- `TeamMember` — team profiles
- `SiteSetting` — editable site configuration

## Production

Use a strong secret key, `DEBUG=False`, restricted hosts, HTTPS, secure cookies, proper CSRF trusted origins, a production email provider and regular database backups.
