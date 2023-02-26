from pydantic import BaseModel, EmailStr, validator


class TunedModel(BaseModel):
    class Config:
        orm_model = True

class UserShow(BaseModel):
    user_id: int
    nick_name: str
    email: EmailStr
    is_admin: bool

class UserCreate(BaseModel):
    nick_name: str
    email: EmailStr
    password: str
