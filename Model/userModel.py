from sqlmodel import SQLModel, Field
from typing import Optional


class User(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = {'schema': 'cricbuzz'}


    id: Optional[int] = Field(None, primary_key=True, nullable=False)
    email: str = Field(unique=True, index=True)
    name: str
    password: str
