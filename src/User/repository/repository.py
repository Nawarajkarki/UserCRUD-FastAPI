from src.entrypoint.database import users
from fastapi import status
from src.User.model.model import User, UserUpdate


class InMemory():
    
    def __init__(self):
        self.users = users
        
    
    def get(self, username:str):
        
        if username == 'all':
            return ({
                "msg" : "Success",
                "User Info" : self.users,
                "status" : status.HTTP_202_ACCEPTED
            })
            
        user = self.users.get(username)

        if user is None:
            return ({
                "msg" : "Failed",
                "Error msg" : "Invalid Username",
                "status" : status.HTTP_404_NOT_FOUND
            })
            
        return ({
            "msg" : "Success",
            "User Info" : self.users[username],
            "status" : status.HTTP_202_ACCEPTED
        })
    
    
    
    def post(self, user : User):
        
        try:
            if self.users.get(user.username) is not None:
                return {
                    "msg" : "Failed",
                    "Error msg" : "User with this username already exists",
                    "status" : status.HTTP_400_BAD_REQUEST
                }
            
            self.users[user.username] = {
                "username" : user.username,
                "email" : user.email,
                "fname" : user.fname,
                "lname" : user.lname,
                "address" : user.address,
                "dob" : user.dob,
                "gender" : user.gender
            }
            
            return ({
                "msg" : "Success",
                "Username" : user.username,
                "status" : status.HTTP_200_OK
            })
        
        except Exception as e:
            return ({
                "msg" : "Failed",
                "Error msg" : f"{e}",
                "status" : status.HTTP_501_NOT_IMPLEMENTED
            })
            
            
    def put(self, username, new_udata : UserUpdate):
        
        user = self.users.get(username)
        if user is None:
            return {
                "msg" : "Failed",
                "Error message" : "User with that username not available",
                'status' : status.HTTP_404_NOT_FOUND
            }
        
        if new_udata.username is not None:
            return {
                "msg" : "Failed",
                "Error message" : "Username cannot be updated",
                'status' : status.HTTP_400_BAD_REQUEST
            }
        
        if new_udata.email is not None:
            user['email'] = new_udata.email

        if new_udata.fname is not None:
            user['fname'] = new_udata.email

        if new_udata.lname is not None:
            user['lname'] = new_udata.lname

        if new_udata.address is not None:
            user['address'] = new_udata.address

        if new_udata.dob is not None:
            user['dob'] = new_udata.dob

        if new_udata.gender is not None:
            user['gender'] = new_udata.gender
            
        
        return {
            "msg" : "Success",
            "User Info" : self.users.get(username),
            'status' : status.HTTP_200_OK
        }
            

    def delete(self, username : str):
        
        user = self.users.get(username)
        if user is None:
            return {
                "msg" : "Failed",
                "Error msg" : "User doesnot exist",
                "status" : status.HTTP_400_BAD_REQUEST
            }
        
        del self.users[username
                       ]
        return {
            "msg" : "Success",
            "User Info" : self.users.get(username),
            "status" : status.HTTP_202_ACCEPTED
        }



repo = InMemory
