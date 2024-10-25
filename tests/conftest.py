from collections.abc import AsyncIterator

import pytest
from dishka import AsyncContainer
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from chat.infrastructure.bootstrap.ioc import setup_ioc


@pytest.fixture(scope="session")
async def acontainer() -> AsyncIterator[AsyncContainer]:
    container = setup_ioc()
    async with container() as c:
        yield c


@pytest.fixture(scope="session")
async def aengine(acontainer: AsyncContainer) -> AsyncEngine:
    return await acontainer.get(AsyncEngine)


@pytest.fixture
async def asession(acontainer: AsyncContainer) -> AsyncSession:
    return await acontainer.get(AsyncSession)
