import strawberry
from typing import Optional
from datetime import datetime

@strawberry.type
class cricbuzzType():
    id: int = None
    team_1: str = None
    team_2: str = None
    date: datetime = None
    venue: str = None

@strawberry.input
class matches_by_id:
    id: int = None

@strawberry.input
class RegisterInput:
    name: str
    email: str
    password: str

@strawberry.input
class LoginInput:
    email: str
    password: str

@strawberry.type
class LoginType:
    email: str
    token: str

@strawberry.input
class create_match:
    team_1: str
    team_2: str
    date: datetime
    venue: str

@strawberry.type
class match_type:
    id: int
    team_1: str
    team_2: str
    date: datetime
    venue: str