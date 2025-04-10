import uuid
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: Optional[str] = None
    fio: Optional[str] = None
    is_active: bool = True
    is_verified: bool = False
    is_superuser: bool = False


class UserCreate(BaseModel):
    email: str
    fio: str
    password: str



class UserUpdate(BaseModel):
    email: Optional[str] = None
    fio: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    is_verified: Optional[bool] = None
    is_superuser: Optional[bool] = None



class User(UserBase):
    id: uuid.UUID

    class Config:
        from_attributes = True


# Модель для сохранения пользователя в БД (с хешированным паролем)
class UserCreateDB(BaseModel):
    hashed_password: str


class UserUpdateDB(BaseModel):
    hashed_password: str



class RefreshSessionCreate(BaseModel):
    refresh_token: uuid.UUID
    expires_in: int
    user_id: uuid.UUID



class RefreshSessionUpdate(BaseModel):
    refresh_token: Optional[uuid.UUID] = None
    expires_in: Optional[int] = None
    user_id: Optional[uuid.UUID] = None



class Token(BaseModel):
    access_token: str
    refresh_token: uuid.UUID
    token_type: str
