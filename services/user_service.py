from typing import Optional
from uuid import UUID
from pydantic import EmailStr
from schemas.user_schema import UserAuth
from models.user_model import User
from core.security import get_password, verify_password


class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        user_in = User(
            username = user.username,
            email = user.email,
            hashed_password = get_password(user.password)
        )
        await user_in.save()
        return user_in
    
    @staticmethod
    async def authenticate(email: EmailStr, password:str)-> Optional[User]:
        user  = await UserService.get_user_by_email(email=email)
        if not user :
            return None
        if not verify_password(password=password,hashed_password = user.hashed_password):
            return None
        
        return user

    @staticmethod
    async def get_user_by_email(email: EmailStr)-> Optional[User]:
        user = await User.find_one(User.email==email)
        return user

    @staticmethod
    async def get_user_by_id(id: UUID)-> Optional[User]:
        user = await User.find_one(User.user_id == id)
        return user
