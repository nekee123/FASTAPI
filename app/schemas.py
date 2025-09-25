from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# User
class UserCreate(BaseModel):
    username: str
    name: Optional[str] = None
    bio: Optional[str] = None

class UserOut(BaseModel):
    uid: str
    username: str
    name: Optional[str] = None
    bio: Optional[str] = None

class UserUpdate(BaseModel):
    name: Optional[str] = None
    bio: Optional[str] = None


# Post
class PostCreate(BaseModel):
    username: str
    content: str

class PostOut(BaseModel):
    uid: str
    content: str
    created_at: datetime
    author: str

class PostUpdate(BaseModel):
    content: Optional[str] = None
