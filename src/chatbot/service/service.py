from src.chatbot.repository.repository import chat_repo
from src.chatbot.model.model import ChatPrompt
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.chatbot.utils.utils import TagsError, PatternError



import random

class ChatOperations():
    
    def __init__(self):
        self.chat_repo = chat_repo()
        
        
    def get(self, prompt : ChatPrompt):
        tag = prompt.tag
        pattern = prompt.prompt
        
        try:
            resp = self.chat_repo.get(tag, pattern)
            # return random.choice(resp)
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                content={
                    'bot' : random.choice(resp)
                }
            )
        
        except TagsError:
            raise HTTPException(
                status_code = status.HTTP_406_NOT_ACCEPTABLE,
                detail = {
                    'msg' : 'Failed',
                    'Error' : f"--{tag}-- didn't match any existing tags."
                }
            )
        
        except PatternError:
            raise HTTPException(
                status_code = status.HTTP_406_NOT_ACCEPTABLE,
                detail = {
                    'msg' : 'Failed',
                    'Error' : f"--{pattern}-- didn't match any existing patterns."
                }
            )

            
        
        


chat_service = ChatOperations