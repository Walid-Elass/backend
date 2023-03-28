from typing import Optional, Literal
from uuid import UUID
from pydantic import BaseModel, Field


class TransactionCreate(BaseModel):
    title: str = Field(..., title="Title", max_length=100, min_length=1)
    description: Optional[str] = Field(..., title="Title", max_length=100, min_length=1)
    type: str
    category: str
    sub_category: str
    amount: float

class TransactionOut(BaseModel):
    transaction_id: UUID
    title: str
    description: str
    type: str
    category: str
    sub_category: str
    amount: float
