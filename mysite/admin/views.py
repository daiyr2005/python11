from pydantic.json_schema import model_json_schema
from  mysite.db.models import *
from  sqladmin import  ModelView


class UserProfileAdmin(ModelView, model = UserProfile):
    column_list = [UserProfile.first_name, UserProfile.last_name]



class RefreshTokenAdmin(ModelView, model=RefreshToken):
    column_list = [RefreshToken.id, RefreshToken.token]


