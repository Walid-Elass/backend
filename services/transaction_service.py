from typing import List
from uuid import UUID
from schemas.transaction_schema import TransactionCreate
from models.user_model import User
from models.transaction_model import Transaction

class TransactionService:

    @staticmethod
    async def list_transactions(user: User) -> List[Transaction]:
        transactions = await Transaction.find(Transaction.owner.id == user.user_id)
        return transactions
    
    @staticmethod
    async def create_transaction(user: User, data: TransactionCreate) -> Transaction:
        transaction = Transaction(**data.dict(),owner=user)
        return await Transaction.insert()
    
    @staticmethod
    async def retrieve_transaction(user: User, transaction_id:UUID) -> Transaction:
        transaction = await Transaction.find_one(Transaction.transaction_id == transaction_id, Transaction.owner.id == user.id)
        return transaction