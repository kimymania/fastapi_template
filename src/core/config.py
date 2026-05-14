import tomllib
from typing import Literal

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
    )

    APP_NAME: str = ""

    @computed_field
    @property
    def version(self) -> str:
        with open("pyproject.toml", "rb") as f:
            data = tomllib.load(f)
            return data["project"]["version"]

    ENV: Literal["development", "staging", "production"] = "development"
    PORT: int = 8000
    WORKERS: int = 1

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = "db"

    @computed_field
    @property
    def sqlalchemy_database_uri(self) -> str:
        path = self.POSTGRES_DB
        if self.ENV == "staging":
            path = "test"
        return str(
            PostgresDsn.build(
                scheme="postgresql+psycopg",
                username=self.POSTGRES_USER,
                password=self.POSTGRES_PASSWORD,
                host=self.POSTGRES_SERVER,
                port=self.POSTGRES_PORT,
                path=path,
            )
        )


settings = Settings()
