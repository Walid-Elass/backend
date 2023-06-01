from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed, Insert, Link, Replace, before_event
from pydantic import Field

class Transaction(Document):
    transaction_id: UUID = Field(default_factory=uuid4)
    title: Indexed(str)
    description: str = None
    type: str
    category: str
    subcategory: str
    amount: float
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner_id: UUID

    # Overriding predefined functions
    def __repr__(self) -> str:
        return f"<User {self.title}>"
    
    def __str__(self) -> str:
        return self.title
    
    def __hash__(self) -> int:
        return hash(self.title)
    
    def __eq__(self, other: object) -> bool :
        if isinstance(other, Transaction):
            return (self.transaction_id == other.transaction_id) and (self.owner_id == other.owner_id)
        return False
    
    @before_event([Replace,Insert])
    def update_updated_at(self):
        self.updated_at = datetime.utcnow()
    
    class Settings:
        name = "transactions_v2"