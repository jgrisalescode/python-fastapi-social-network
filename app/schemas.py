from pydantic import BaseModel, EmailStr
from datetime import date, datetime

# Request form the user
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass

# Response to the user
class Post(PostBase):
    created_at: datetime

    # Pydantic works with dict, but we passed sqlalchemy model, we need this
    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr

    # Pydantic works with dict, but we passed sqlalchemy model, we need this
    class Config:
        orm_mode = True