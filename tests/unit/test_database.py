from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession


async def test_health_engine(aengine: AsyncEngine) -> None:
    async with aengine.connect() as conn:
        result = await conn.execute(text("select 1"))
        assert result.scalar() == 1


async def test_health_session(asession: AsyncSession) -> None:
    stmt = await asession.execute(text("select 1"))
    assert stmt.scalar() == 1
