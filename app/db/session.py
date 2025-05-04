from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import setting

engine = create_async_engine(setting.DATABASE_URL_USERS, echo=True, future=True)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


from typing import AsyncGenerator

async def get_db() -> AsyncGenerator:
    async with SessionLocal() as session:
        yield session