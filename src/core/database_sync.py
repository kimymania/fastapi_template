from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from src.core.config import settings

engine = create_engine(settings.sqlalchemy_database_uri)
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    check_same_thread=False,
    echo=bool(settings.ENV == "development"),
)


def get_db() -> Generator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SessionDep = Annotated[Session, Depends(get_db)]


class Base(DeclarativeBase): ...
