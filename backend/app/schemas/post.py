from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class PostBase(BaseModel):
    title: str
    content: str
    tags: Optional[str] = None

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    title: str = None
    content: str = None
    tags: Optional[str] = None

class Post(PostBase):
    id: int
    author_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True