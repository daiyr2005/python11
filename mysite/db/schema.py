from  pydantic import  BaseModel, EmailStr
from typing import Optional
from  datetime import date
from .models import UserRoleChoice



class UserProfileInputSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email:EmailStr
    password:str
    photo:str
    age: Optional[int]
    phone_number: str




class UserProfileOutSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email:EmailStr
    password:str
    photo:str
    age: Optional[int]
    phone_namber: str
    user_role: UserRoleChoice
    date_registered: date
    is_active: bool

class UserLoginSchema(BaseModel):
    username: str
    password: str




