from pydantic import BaseModel


class ChatPrompt(BaseModel):
    tag : str
    prompt : str | None = None