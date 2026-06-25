from pydantic import BaseModel, Field
# Импортируем заранее созданный экземпляр класса Fake
from tools.fakers import fake

# Добавили суффикс Schema вместо Dict
class TokenSchema(BaseModel):  # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры аутентификационных токенов.
    """
    token_type: str = Field(alias="tokenType")  # Использовали alise
    access_token: str = Field(alias="accessToken")  # Использовали alise
    refresh_token: str = Field(alias="refreshToken")  # Использовали alise


# Добавили суффикс Schema вместо Dict
class LoginResponseSchema(BaseModel):  # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры ответа аутентификации.
    """
    token: TokenSchema


class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str = Field(default_factory=fake.email)  # Добавили генерацию случайного email
    password: str = Field(default_factory=fake.password)  # Добавили генерацию случайного пароля

class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    # Добавили генерацию случайного предложения
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)