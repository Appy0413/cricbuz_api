from Model.cricbuzzModel import match_info
from config import db
from sqlalchemy.sql import select
from sqlalchemy import and_
from sqlalchemy import asc
from sqlalchemy import inspect

class cricbuzzRepository:
    @staticmethod
    async def get_match_schedule():
        async with db as session:
            # Build conditions from query_params
            # Assuming match_info is your SQLAlchemy model class
            query = select(match_info)
            result = await session.execute(query)
            return result.scalars().all()
        
    @staticmethod
    async def get_match_detail_by_id(match_id: int):
        async with db as session:
            stmt = select(match_info).where(match_info.id == match_id)
            result = await session.execute(stmt)
            info = result.scalars().first()
            return info