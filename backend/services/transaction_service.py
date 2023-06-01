from typing import List
from uuid import UUID
from schemas.transaction_schema import TransactionCreate, TransactionUpdate
from models.transaction_model import Transaction
from fastapi import HTTPException
import csv
import io


class TransactionService:

    @staticmethod
    async def list_transactions(current_user_id: UUID) -> List[Transaction]:
        transactions = await Transaction.find(Transaction.owner_id == current_user_id).to_list()
        return transactions
    
    @staticmethod
    async def create_transaction(current_user_id: UUID, data: TransactionCreate) -> Transaction:
        transaction = Transaction(**data.dict(),owner_id=current_user_id)
        return await transaction.insert()
    
    @staticmethod
    async def retrieve_transaction(current_user_id: UUID, transaction_id:UUID) -> Transaction:
        transaction = await Transaction.find_one(Transaction.transaction_id == transaction_id, Transaction.owner_id == current_user_id)
        return transaction
    
    @staticmethod
    async def update_transaction(current_user_id: UUID, transaction_id:UUID, data: TransactionUpdate) -> Transaction:
        transaction = await TransactionService.retrieve_transaction(current_user_id,transaction_id)
        await transaction.update({"$set" : data.dict(exclude_unset=True)})

        await transaction.save()
        return transaction

    @staticmethod
    async def delete_transaction(current_user_id: UUID, transaction_id:UUID) -> Transaction:
        transaction = await TransactionService.retrieve_transaction(current_user_id,transaction_id)
        if transaction:
            await transaction.delete()
        
        return None
    
    @staticmethod
    async def import_transactions(current_user_id: UUID, file):
        if file.filename.endswith('.csv'):
            contents = await file.read()
            reader = csv.DictReader(io.StringIO(contents.decode("utf-8")))

            transactions_to_insert: List[Transaction] = []

            for row in reader:
                # Parse CSV row into Transaction data
                transaction_data = {
                    "title": row.get("title"),
                    "description": row.get("description"),
                    "type": row.get("type"),
                    "category": row.get("category"),
                    "subcategory": row.get("subcategory") if row.get("subcategory") else 'Not Specified' ,
                    "amount": float(row.get("amount")),
                    "owner_id": current_user_id
                }
                
                # Create Transaction instance
                transaction = Transaction(**transaction_data)
                

                # Add Transaction instance to list
                transactions_to_insert.append(transaction)
            
            inserted_count = await Transaction.insert_many(transactions_to_insert)

            return {"message": f"Inserted {len(transactions_to_insert)} transactions."}
        else:
            raise HTTPException(status_code=400, detail="Invalid file format. Please upload a '.csv' file.")



            