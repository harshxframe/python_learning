from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    UserName: str
    @field_validator('UserName')
    def validate_name(cls, v):
        if len(v) <8:
            raise ValueError('UserName must be at least 8 characters long')
        return v

class SignUP(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def validate_password(cls, v):
        if v.password != v.confirm_password:
            raise ValueError('Passwords do not match')
        return v


result = SignUP(password='1234567890', confirm_password='1234567890')
print(result)