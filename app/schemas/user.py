from pydantic import BaseModel, EmailStr, constr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: constr(min_length=8, max_length=100)

class UserLogin(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True