# Why split Django settings into base, dev, and prod?

Splitting Django settings into `base.py`, `dev.py`, and `prod.py` reduces risk and makes deployment safer and clearer.

## Why this matters

- **Security by default**: production-only requirements (for example `SECRET_KEY`, `DATABASE_URL`, and production hosts) are isolated to `prod.py`, reducing accidental local defaults leaking into production.
- **Cleaner configuration**: shared settings live in `base.py`, while environment-specific differences are explicit in `dev.py` and `prod.py`.
- **Safer local development**: `dev.py` defaults to SQLite and debug mode without requiring production environment variables.
- **Predictable deployment behavior**: entrypoints can explicitly target `config.settings.dev` (local tooling) and `config.settings.prod` (runtime server processes).

## Operational impact

- Local commands default to `config.settings.dev`.
- ASGI/WSGI entrypoints default to `config.settings.prod` and still support overriding via `DJANGO_SETTINGS_MODULE`.
- Heroku (or any platform) can continue setting `DJANGO_SETTINGS_MODULE` explicitly if desired.
