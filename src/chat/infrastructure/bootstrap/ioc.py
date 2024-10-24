from dishka import AnyOf, AsyncContainer, Provider, Scope, make_async_container
from sqlalchemy.ext.asyncio import AsyncSession

from chat.application.common.uow import UoWProtocol
from chat.infrastructure.bootstrap.config import PostgresConfig, load_config
from chat.infrastructure.persistence.provider import (
    create_aengine,
    new_asession,
    session_factory,
)


def config_provider() -> Provider:
    config = load_config()
    provider = Provider()
    provider.provide(
        lambda: config.postgres, scope=Scope.APP, provides=PostgresConfig
    )
    return provider


def db_provider() -> Provider:
    provider = Provider()
    provider.provide(create_aengine, scope=Scope.APP)
    provider.provide(session_factory, scope=Scope.APP)
    provider.provide(
        new_asession,
        scope=Scope.REQUEST,
        provides=AnyOf[UoWProtocol, AsyncSession],
    )
    return provider


def setup_providers() -> list[Provider]:
    return [
        config_provider(),
        db_provider(),
    ]


def setup_ioc() -> AsyncContainer:
    providers = setup_providers()
    container = make_async_container(*providers)
    return container
