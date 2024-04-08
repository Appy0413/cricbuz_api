from Repository.cricbuzzRepository import cricbuzzRepository
from schema import cricbuzzType,create_match,match_type
from Model.cricbuzzModel import match_info
from Repository.userRepository import UserRepository

class cricbuzzService:

    @staticmethod
    async def create_match(user_data: create_match):
        user = match_info()
        user.team_1 = user_data.team_1
        user.team_2 = user_data.team_2
        user.date = user_data.date
        user.venue = user_data.venue
        await UserRepository.create(user)

        return f"successfully registered data!"

    @staticmethod
    async def get_match_schedule():      
        list_match_info = await cricbuzzRepository.get_match_schedule()
        for i in list_match_info:
            print(i)
        return [match_type(id=i.id,team_1=i.team_1, team_2=i.team_2, venue=i.venue, date=i.date) for i in list_match_info]
    

    @staticmethod
    async def get_match_detail_by_id(id):      
        note = await cricbuzzRepository.get_match_detail_by_id(id)
        return match_type(id=note.id,team_1=note.team_1, team_2=note.team_2, venue=note.venue, date=note.date)