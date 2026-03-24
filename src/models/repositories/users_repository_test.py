import pytest
from .users_repository import UsersRepository

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