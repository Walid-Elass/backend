from fastapi import APIRouter
from api.api_v1.handlers import transactions

router = APIRouter()

router.include_router(transactions.transactions_router, prefix="/transactions",tags=['transactions'])

@router.get("/alive",tags=['Ping'])
async def alive_check():
    return {"status": "Transactions API is alive"}