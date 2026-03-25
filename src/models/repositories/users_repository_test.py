import pytest
import pytest_asyncio
from .users_repository import UsersRepository
from src.models.settings.database_connection_handler import engine
from src.models.settings.metadata import metadata
from src.models.entities.users import Users  # registra a tabela no metadata


@pytest_asyncio.fixture(autouse=True)
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)


@pytest.mark.asyncio
async def test_insert_user():
  new_user = {
      "user_name": "testName",
      "age": 99,
      "uf": "SP"
  }
  repo = UsersRepository()
  await repo.insert_users(new_user)
    
@pytest.mark.asyncio
async def test_get_users_by_name():
  repo = UsersRepository()
  response = await repo.get_users_by_name("testName")