from pydantic import BaseModel, Field



class CommonResponse(BaseModel):
    status:bool
    message:str