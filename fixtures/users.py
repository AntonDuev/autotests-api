
from pydantic import BaseModel, EmailStr

from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema
from clients.private_http_builder import AuthenticationUserSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:  # Быстрый доступ к email пользователя
        return self.request.email

    @property
    def password(self) -> str:  # Быстрый доступ к password пользователя
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(
            email = self.request.email,
            password = self.request.password
        )