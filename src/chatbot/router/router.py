from fastapi import APIRouter
from src.chatbot.model.model import ChatPrompt
from src.chatbot.service.service import chat_service

chatbot = APIRouter(prefix = '/api/v1/chatbot', tags=['ChatBot'])


@chatbot.get('/')
def response_to_user(prompt : ChatPrompt):
    return chat_service().get(prompt = prompt)
    
