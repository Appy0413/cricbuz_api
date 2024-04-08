from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime


class match_info(SQLModel, table=True):
    __tablename__ = "matches"
    __table_args__ = {'schema': 'cricbuzz'}
    id: Optional[int] = Field(default=None, primary_key=True)
    team_1: Optional[str]
    team_2: Optional[str]
    date: Optional[datetime] 
    venue: Optional[str]
