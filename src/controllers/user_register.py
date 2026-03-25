from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from .interfaces.user_register import UserRegisterInterface
class UserRegister(UserRegisterInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self._users_repository = users_repository

    async def register_user(self, user_data: dict) -> dict:
        self._validate_user_data(user_data)
        await self.__registry_user(user_data)
        return self.__format__response(user_data)

    def _validate_user_data(self, user_data: dict) -> None:
        age = user_data["age"]
        uf = user_data["uf"].upper()

        if uf not in ["MG", "BA", "CE", "SC", "MT"]:
            raise HttpBadRequestError("Invalid state")

        if age < 0 or age > 120:
            raise HttpBadRequestError("Invalid age")

    async def __registry_user(self, user_data: dict) -> None:
        await self._users_repository.insert_users(user_data)

    def __format__response(self, user_data: dict) -> dict:
        return {
            "type": "USERS",
            "count": 1,
            "attributes": user_data
        }