from typing import List, Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed, Insert, Link, Replace, before_event
from pydantic import Field
from models.user_model import User

class Category(Document):
    category_id: UUID = Field(default_factory=uuid4)
    title: Indexed(str)
    description: Optional[str] = None
    subcategories: List[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Overriding predefined functions
    def __repr__(self) -> str:
        return f"<User {self.title}>"
    
    def __str__(self) -> str:
        return self.title
    
    def __hash__(self) -> int:
        return hash(self.title)
    
    @before_event([Replace,Insert])
    def update_updated_at(self):
        self.updated_at = datetime.utcnow()
    
    class Settings:
        name = "categories"