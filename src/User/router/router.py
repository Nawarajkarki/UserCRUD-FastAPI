from fastapi import APIRouter,status
from src.User.service.service import user_service
from src.User.model.model import User, UserUpdate






user = APIRouter(prefix="/api/v1/users", tags=['USERS'])


@user.get('/')
def get_all_user():
    return user_service().get(username="all")

@user.get('/{username}')
def get_user(username:str):
    return user_service().get(username=username)

@user.post('/')
def create_user(user:User):
    return user_service().post(user=user)

@user.put('/{username}')
def update_userinfo(username:str, new_udata : UserUpdate):
    return user_service().put(username = username, new_udata = new_udata)

@user.delete('/{username}')
def delete_user(username : str):
    return user_service().delete(username = username)