# FastAPI Template

FastAPI project template

## Stack

Python 3.14+

### Backend
- FastAPI with async routes
- Database: SQLAlchemy (Async) + Alembic
- Server: Granian

### Dev dependencies
- Pre-commit: prek
- Testing: httpx + pytest + coverage

### Utilities
- Package management: uv 
- Docker

## Project layout

```
src
    main.py : FastAPI app & lifespan, Granian server settings
    core
        config.py : configurations
        database.py : DB initialization, Base model, session dependency
    features - Feature-based, similar to Django applications
```
