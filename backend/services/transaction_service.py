from typing import List
from uuid import UUID
from schemas.transaction_schema import TransactionCreate, TransactionUpdate
from models.user_model import User
from models.transaction_model import Transaction

class TransactionService:

    @staticmethod
    async def list_transactions(current_user: User) -> List[Transaction]:
        transactions = await Transaction.find(Transaction.owner.id == current_user.id).to_list()
        return transactions
    
    @staticmethod
    async def create_transaction(current_user: User, data: TransactionCreate) -> Transaction:
        transaction = Transaction(**data.dict(),owner=current_user)
        return await transaction.insert()
    
    @staticmethod
    async def retrieve_transaction(current_user: User, transaction_id:UUID) -> Transaction:
        transaction = await Transaction.find_one(Transaction.transaction_id == transaction_id, Transaction.owner.id == current_user.id)
        return transaction
    
    @staticmethod
    async def update_transaction(current_user: User, transaction_id:UUID, data: TransactionUpdate) -> Transaction:
        transaction = await TransactionService.retrieve_transaction(current_user,transaction_id)
        await transaction.update({"$set" : data.dict(exclude_unset=True)})

        await transaction.save()
        return transaction

    @staticmethod
    async def delete_transaction(current_user: User, transaction_id:UUID, data: TransactionUpdate) -> Transaction:
        transaction = await TransactionService.retrieve_transaction(current_user,transaction_id)
        if transaction:
            await transaction.delete()
        
        return None