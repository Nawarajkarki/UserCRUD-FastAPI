from pydantic import BaseModel, constr, EmailStr, validator
from datetime import date


class User(BaseModel):
    username : constr(min_length=4, max_length=10)
    email : EmailStr
    fname : constr(min_length=3, max_length=20)
    lname : constr(min_length=2, max_length=20)
    address : str
    dob : str
    gender : constr(min_length=1, max_length=6)
    
    
    
    @validator('dob')
    def validate_DOB(cls, value):
        try:
            return date.fromisoformat(value)

        except ValueError:
            raise ValueError ("DOB needs to be in YYYY-MM--DD Format")



class UserUpdate(BaseModel):
    username : constr(min_length=4, max_length=10) = None
    email : EmailStr = None
    fname : constr(min_length=3, max_length=20) = None
    lname : constr(min_length=2, max_length=20) = None
    address : str = None
    dob : str = None
    gender : constr(min_length=1, max_length=6) = None
    

    
    @validator('dob')
    def validate_DOB(cls, value):
        if value is not None:
            try:
                return date.fromisoformat(value)

            except ValueError:
                raise ValueError ("DOB needs to be in YYYY-MM--DD Format")

