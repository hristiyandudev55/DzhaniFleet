from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, field_validator


class BaseConfig(BaseModel):
    model_config = {"from_attributes": True}


class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: str
    role: str


class TokenData(BaseModel):
    user_identifier: int | None = None
    user_email: str | None = None


class UserBase(BaseConfig):
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(min_length=4, max_length=30, examples=["Parola123!"])

    @field_validator("password")
    def validate_password(cls, value):
        if not (
            any(c.isupper() for c in value)
            and any(c.islower() for c in value)
            and any(c.isdigit() for c in value)
            and not any(c.isspace() for c in value)
        ):
            raise ValueError(
                "Password must containt at least"
                "one uppercase letter, one lowercase letter, "
                "one number, one special character, "
                "and must not contain any spaces"
            )
        return value


class UserResponse(UserBase):
    id: UUID
    email: EmailStr
    role: str


class UserRegisterResponse(BaseConfig):
    email: EmailStr
    role: str


class UserUpdate(UserBase):
    pass


class UserRole(BaseModel):
    role: str
