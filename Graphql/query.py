from typing import List, Optional
from strawberry.types import Info
import strawberry
from Service.cricbuzzService import cricbuzzService
from schema import cricbuzzType, matches_by_id
from Middleware.JWTBearer import IsAuthenticated
from schema import match_type

@strawberry.type
class Query:

    @strawberry.field(permission_classes=[IsAuthenticated])
    async def get_match_detail_by_id(self, id: int) -> match_type:
        return await cricbuzzService.get_match_detail_by_id(id)