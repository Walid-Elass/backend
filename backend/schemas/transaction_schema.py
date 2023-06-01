from datetime import datetime
from typing import Optional, Literal
from uuid import UUID
from pydantic import BaseModel, Field


class TransactionCreate(BaseModel):
    title: str = Field(..., title="Title", max_length=1000, min_length=1)
    description: Optional[str] = Field(..., title="Title", max_length=1000, min_length=1)
    type: str
    category: str
    subcategory: Optional[str] = "Not Specified"
    amount: float

class TransactionUpdate(BaseModel):
    title: Optional[str] = Field(..., title="Title", max_length=100, min_length=1)
    description: Optional[str] = Field(..., title="Title", max_length=100, min_length=1)
    type: Optional[str]
    category: Optional[str]
    subcategory: Optional[str]
    amount: Optional[float]

class TransactionOut(BaseModel):
    transaction_id: UUID
    title: str
    description: str
    type: str
    category: str
    subcategory: str
    amount: float
    created_at: datetime
