from fastapi import FastAPI, Request, status, HTTPException
from fastapi.responses import JSONResponse
from src.User.router.router import user
from src.Blog.router.router import blog
from src.chatbot.router.router import chatbot

from src.chatbot.utils.utils import TagsError, PatternError


app = FastAPI()


app.include_router(user)
app.include_router(blog)
app.include_router(chatbot)



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
    
    


       
@app.exception_handler(PatternError)
async def pattern_error_handler(request : Request, exc : PatternError):
    return JSONResponse(
        status_code = 418,
        # status_code = status.HTTP_406_NOT_ACCEPTABLE,
        content={
            "msg" : f"Oops Pattern --{exc.pattern} didn't match"
        }
    )
    
    
@app.exception_handler(TagsError)
async def tag_error_handler(request:Request, exc:TagsError):
    return JSONResponse(
        status_code= 418,
        # status_code= status.HTTP_406_NOT_ACCEPTABLE,
        content={
            "msg" : f"Oops Tag --{exc.tag} didn't match"
            
        }
    )