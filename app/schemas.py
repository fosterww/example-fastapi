from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from typing import Annotated
from pydantic import BaseModel, Field

class UserBase(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config():
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class PostBase(BaseModel):
    title: str
    content: str
    published: bool=True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    user_id: int
    user: UserOut

    class Config():
        from_attributes = True

class PostOut(BaseModel):
    post: Post
    votes: int

    class Config():
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
    
class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(strict=True, le=1)] 
