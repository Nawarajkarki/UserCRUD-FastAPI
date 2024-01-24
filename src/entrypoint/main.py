from fastapi import FastAPI, status
from src.User.router.router import user
from src.Blog.router.router import Blog

app = FastAPI()

app.include_router(user)
app.include_router(Blog)

@app.get('/')
def welcome():
    return ({
        "message" : "Welcome to my service.", 
        'status' : status.HTTP_200_OK
    })


@app.get('/{username}')
def welcome(username : str):
    username = username
    return ({
        "message" : f"Hi {username}!!!", 
        "Greetings" : "Welcome to my service.", 
        "status" : status.HTTP_202_ACCEPTED
    })    
    



# @app.get('/user/{username}')
# def get(username:str):
        
#     user = users.get(username)
#     if user is None:
#         return ({
#             "msg" : "Failed",
#             "Error msg" : "Invalid Username",
#             "status" : status.HTTP_404_NOT_FOUND
#         })
    
    
#     return ({
#         "msg" : "Success",
#         "User Info" : users[username]
#     })