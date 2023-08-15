from pydantic import BaseModel, EmailStr
from typing import Optional, Sequence
from uuid import UUID
from datetime import datetime


class UserBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr] = None


class UserCreate(UserBase):
    email: EmailStr


class UserUpdate(UserBase):
    ...

class UserInDBBase(UserBase):
    id: Optional[int] = None
    uuid: Optional[UUID] = None
    created_at: Optional[datetime] = None
    last_modified: Optional[datetime] = None

    class ConfigDict:
        from_attributes = True


class UserSchema(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    pass

class UserSearchResults(BaseModel):
    results: Sequence[UserSchema] = None
    


