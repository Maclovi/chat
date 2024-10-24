from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from chat.infrastructure.bootstrap.config import PostgresConfig


async def create_aengine(config: PostgresConfig) -> AsyncIterator[AsyncEngine]:
    engine = create_async_engine(
        config.db_uri,
        echo=True,
        pool_size=15,
        max_overflow=15,
        connect_args={"connect_timeout": 5},
    )
    yield engine
    await engine.dispose()


def session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(engine, autoflush=False, expire_on_commit=False)


async def new_asession(
    session_factory: async_sessionmaker[AsyncSession],
) -> AsyncIterator[AsyncSession]:
    async with session_factory() as session:
        yield session
