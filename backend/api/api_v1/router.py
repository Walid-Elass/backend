from fastapi import APIRouter
from api.api_v1.handlers import user
from api.auth.jwt import auth_router
from api.api_v1.handlers import transactions

router = APIRouter()

router.include_router(user.user_router, prefix="/users", tags=["users"])
router.include_router(auth_router, prefix='/auth', tags=["auth"])
router.include_router(transactions.transactions_router, prefix="/transactions",tags=['transactions'])

@router.get("/alive")
async def alive_check():
    return {"status": "Authentication API is alive"}