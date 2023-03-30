from fastapi import APIRouter, Depends, HTTPException, status
from api.dependencies.user_dependencies import get_current_user
from models.user_model import User
from schemas.user_schema import  UserAuth, UserOut, UserUpdate
from services.user_service import UserService

import pymongo

user_router = APIRouter()

@user_router.post('/create', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException (
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = "User with this email or username already exists"
        )
    
@user_router.get('/me',summary="Get details of currently logged user", response_model=UserOut)
async def retreive_current_user(user: User = Depends(get_current_user)):
    return user
         

@user_router.put('/update', summary="Update a user's information", response_model=UserOut)
async def update_user(data: UserUpdate, user : User = Depends(get_current_user)):
    try:
        return await UserService.update_user(user.id, data)
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User does not exist"
        )