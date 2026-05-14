from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.config import settings
from src.features.routers import router as api_routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    ...
    yield
    ...


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.version,
    lifespan=lifespan,
    docs_url=None if settings.ENV == "production" else "/docs",
    redoc_url=None if settings.ENV == "production" else "/redoc",
    openapi_url=None if settings.ENV == "production" else "/openapi.json",
)
app.include_router(api_routers)


@app.get("/")
def main():
    return "Hello"

