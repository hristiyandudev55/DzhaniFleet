
from pydantic import BaseModel


class BaseConfig(BaseModel):
    model_config = {"from_attributes": True}


class Token(BaseModel):
    pass


class TokenData(BaseModel):
    pass


class UserBase(BaseConfig):
    pass


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    pass


class UserRegisterResponse(BaseConfig):
    pass


class UserUpdate(UserBase):
    pass


class UserRole(BaseModel):
    pass
