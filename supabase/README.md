# Supabase database setup

Attribute Procedurals uses **Supabase PostgreSQL as the production database** while Django remains the application/backend layer.

## 1. Create the Supabase project

In Supabase, create a project and keep the database password safe.

## 2. Get the database connection string

Open **Connect** in the Supabase dashboard and copy the PostgreSQL connection string. For a Django deployment, the Transaction Pooler connection is a practical option. Put it in `.env` as `DATABASE_URL`.

Never commit `.env` to Git.

## 3. Let Django own the schema

Run:

```bash
python manage.py makemigrations
python manage.py migrate
```

This creates the tables for:

- contact_messages
- projects
- research_projects
- insights
- technologies
- team_members
- site_settings

The SQL file in this directory is provided as a reference/inspection schema. Django migrations are the source of truth for the application schema.

## 4. Verify the connection

```bash
python manage.py check
python manage.py showmigrations
```

## Architecture

```text
Visitor
  |
  v
Django Website
  |
  +--> Django Admin
  |
  +--> Supabase PostgreSQL
  |
  +--> Email Provider
```

Supabase can later also provide Storage and Auth, but the current implementation keeps authentication under Django Admin and uses Supabase primarily as the managed PostgreSQL database.
