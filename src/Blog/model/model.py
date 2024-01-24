from pydantic import BaseModel, validator, constr
from src.User.repository.repository import UserRepository


class Blog(BaseModel):
    
    author : constr(min_length=4, max_length=10) # Try making author to be only valid username
    title : constr(min_length=10)
    content : constr(min_length=10)
    
    
class BlogUpdate(BaseModel):
    
    author : constr(min_length=4, max_length=10) = None
    title : constr(min_length=10) = None
    content : constr(min_length=10) = None
    
    
    