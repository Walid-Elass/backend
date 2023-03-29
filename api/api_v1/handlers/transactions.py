from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from api.dependencies.user_dependencies import get_current_user
from services.transaction_service import TransactionService
from schemas.transaction_schema import TransactionOut, TransactionCreate, TransactionUpdate
from models.user_model import User

transactions_router = APIRouter()

@transactions_router.get("/all", summary="Get all transactions of the user", response_model=List[TransactionOut])
async def get_all_transactions(current_user: User = Depends(get_current_user)):
    return await TransactionService.list_transactions(current_user)

@transactions_router.post('/create',summary="Create a transaction", response_model=TransactionCreate)
async def create_transaction(data: TransactionCreate,current_user: User = Depends(get_current_user)):
    return await TransactionService.create_transaction(current_user,data)

@transactions_router.get('/{transaction_id}',summary="Get a transaction by id",response_model=TransactionOut)
async def retrieve(transaction_id:UUID,current_user: User = Depends(get_current_user)):
    return await TransactionService.retrieve_transaction(current_user,transaction_id)

@transactions_router.put('/{transaction_id}',summary='Update a transaction by transaction_id', response_model=TransactionOut)
async def update_transaction(transaction_id:UUID, data: TransactionUpdate ,current_user: User=Depends(get_current_user)):
    return await TransactionService.update_transaction(current_user,transaction_id,data)

@transactions_router.delete('/{transaction_id}',summary="Delete a transaction by transaction_id")
async def delete_transaction(transaction_id:UUID ,current_user: User=Depends(get_current_user)):
    return await TransactionService.update_transaction(current_user,transaction_id)