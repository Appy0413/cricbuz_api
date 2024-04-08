import strawberry
from Service.authentication import AuthenticationService
from Service.cricbuzzService import cricbuzzService
from schema import RegisterInput, LoginInput, LoginType,create_match,match_type
from Service.cricbuzzService import cricbuzzService
from typing import List


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def login(self, login_data: LoginInput) -> LoginType:
        return await AuthenticationService.login(login_data)

    @strawberry.mutation
    async def register(self, register_data: RegisterInput) -> str:
        return await AuthenticationService.register(register_data)

    @strawberry.mutation
    async def add_match(self, create_match_input: create_match) -> str:
        return await cricbuzzService.create_match(create_match_input)
    
    @strawberry.mutation
    async def get_match_schedule(self) -> List[match_type]:
        return await cricbuzzService.get_match_schedule()