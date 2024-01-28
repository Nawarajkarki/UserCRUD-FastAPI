from src.entrypoint.database import users
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from src.User.model.model import User, UserUpdate


class InMemory():
    
    def __init__(self):
        self.users = users
        
    
    def get(self, username:str, status_code=status.HTTP_202_ACCEPTED):
        
        if username == 'all':
            return ({
                "msg" : "Success",
                "User Info" : self.users,
            })
            
        user = self.users.get(username)

        if user is None:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = {
                    "msg" : "Failed",
                    "Error mag" : "f User with username:{username} doesn't exist"
                }
            )
        
        return JSONResponse(
            content = {
                "msg" : "Success",
                "User Info" : self.users[username]
            },
        )
    
    
    def post(self, user : User):
        
        try:
            if self.users.get(user.username) is not None:
                raise HTTPException(
                    status_code = status.HTTP_404_NOT_FOUND,
                    detail = {
                        "msg" : "Failed",
                        "Error msg" : f"User with username : {user.username} already exist."
                    }
                )
            
            self.users[user.username] = {
                "username" : user.username,
                "email" : user.email,
                "fname" : user.fname,
                "lname" : user.lname,
                "address" : user.address,
                "dob" : user.dob,
                "gender" : user.gender
            }
            
            return JSONResponse(
                content = {
                    "msg" : "Success",
                    "Username" : user.username,
                },
            )
        
        except Exception as e:
            raise HTTPException (
                status_code =  status.HTTP_501_NOT_IMPLEMENTED,
                detail = {
                    "msg" : "Failed",
                    "Error msg" : f"{e}",
                },
            )
            
            
    def put(self, username, new_udata : UserUpdate):
        
        user = self.users.get(username)
        if user is None:
            raise HTTPException( 
                detail = {
                    "msg" : "Failed",
                    "Error message" : "User with that username not available"
                },
                status_code = status.HTTP_404_NOT_FOUND
            )
        
        if new_udata.username is not None:
            raise HTTPException( 
                detail = {
                    "msg" : "Failed",
                "Error message" : "Username cannot be updated"
                },
                status_code = status.HTTP_400_BAD_REQUEST
            )
            
        
        if new_udata.email is not None:
            user['email'] = new_udata.email

        if new_udata.fname is not None:
            user['fname'] = new_udata.fname

        if new_udata.lname is not None:
            user['lname'] = new_udata.lname

        if new_udata.address is not None:
            user['address'] = new_udata.address

        if new_udata.dob is not None:
            user['dob'] = new_udata.dob

        if new_udata.gender is not None:
            user['gender'] = new_udata.gender
            
        
        return JSONResponse(
            content = {
                "msg" : "Success",
                "User Info" : self.users.get(username)
            }
        )

    def delete(self, username : str):
        
        user = self.users.get(username)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                content = {
                    "msg" : "Failed",
                    "Error msg" : "User doesnot exist"
                },
            )
            
        
        del self.users[username]
        
        return JSONResponse(
            content = {
                "msg" : "success",
                "User Info" : self.users.get(username)
            },
        )
        


UserRepository = InMemory
