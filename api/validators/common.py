from pydantic import BaseModel

class ListAPI(BaseModel):
    page:int = 1,
    limit:int = 10