from fastapi import APIRouter

transactions_router = APIRouter()

@transactions_router.get("/all")
async def get_all_transactions():
    return 