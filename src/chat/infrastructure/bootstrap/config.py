from dataclasses import dataclass
from os import environ


@dataclass(slots=True, kw_only=True)
class PostgresConfig:
    host: str
    port: str
    user: str
    password: str
    db: str

    @property
    def db_uri(self) -> str:
        return f"postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


@dataclass(slots=True, kw_only=True)
class Config:
    postgres: PostgresConfig


def load_config() -> Config:
    return Config(
        postgres=PostgresConfig(
            host=environ["POSTGRES_HOST"],
            port=environ["POSTGRES_PORT"],
            user=environ["POSTGRES_USER"],
            password=environ["POSTGRES_PASSWORD"],
            db=environ["POSTGRES_DB"],
        )
    )
