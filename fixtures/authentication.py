from fixtures.users import UserFixture
import pytest
from pydantic import BaseModel, EmailStr
from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema



@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()

@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()


# Фикстура для создания пользователя
@pytest.fixture
# Используем фикстуру public_users_client, которая создает нужный API клиент
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)  # Возвращаем все нужные данные

@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    return get_private_users_client(
        user=function_user.authentication_user
    )