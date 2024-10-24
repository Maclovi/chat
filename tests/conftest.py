import pytest
from dishka import AsyncContainer

from chat.infrastructure.bootstrap.ioc import setup_ioc


@pytest.fixture(scope="session")
def container() -> AsyncContainer:
    return setup_ioc()
