from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from core.config import settings

engine = create_async_engine(settings.sqlalchemy_database_uri)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    echo=bool(settings.ENV == "development"),
)


async def get_db() -> AsyncGenerator[AsyncSession]:
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()


SessionDep = Annotated[AsyncSession, Depends(get_db)]


class Base(DeclarativeBase, AsyncAttrs): ...
