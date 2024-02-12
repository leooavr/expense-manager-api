from pydantic import BaseModel

class EmailModel(BaseModel):
    to_email: str
    subject: str
    message: str