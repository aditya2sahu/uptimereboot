from pydantic import BaseModel, EmailStr , Field



class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(max_length=16, min_length=8)
    name:str


class UserResponse(BaseModel):
    email: EmailStr
    name: str
    token: str


class User(BaseModel):
    id:int
    email:str
    password:str
    is_verified:bool
    is_active:bool

    model_config = {
        "from_attributes": True
    }