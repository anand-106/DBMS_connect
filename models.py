from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Pydantic model for creating a user
class UserCreate(BaseModel):
    name: str
    email: str

# Pydantic model for the response
class UserResponse(UserCreate):
    id: int

    class Config:
        orm_mode = True
