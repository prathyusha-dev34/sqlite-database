from pydantic import BaseModel, EmailStr


# Register Schema
class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str


# Login Schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Response Schema
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True