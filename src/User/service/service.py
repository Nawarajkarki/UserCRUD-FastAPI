from src.User.repository.repository import UserRepository



class UserOperations():
    
    def __init__(self):
        self.user_repo = UserRepository()
    
    
    def get(self, username:str):
        response = self.user_repo.get(username=username)
        return response
    
    def post(self, user):
        response = self.user_repo.post(user=user)
        return response
    
    def put(self, username:str, new_udata):
        response = self.user_repo.put(username=username, new_udata = new_udata)
        return response
    
    def delete(self,username:str):
        response = self.user_repo.delete(username=username)
        return response


        



user_service = UserOperations