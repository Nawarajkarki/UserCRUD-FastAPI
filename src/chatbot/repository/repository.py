from src.entrypoint.database import chat_responses
from src.chatbot.model.model import ChatPrompt

from src.chatbot.utils.utils import *
import random

class ChatRepo():
    
    def __init__(self):
        self.chat_responses = chat_responses
        
    def get(self, tag:str, pattern:str):
            for each in self.chat_responses:
            
                if tag.lower() == each['tag'].lower():
                    for each_pattern in each['patterns']:
                        if pattern.lower() == each_pattern.lower():
                            return each['responses']
                    

                    raise PatternError(pattern=pattern)
            raise TagsError(tag=tag)
        

        
                
    

        
        


chat_repo = ChatRepo