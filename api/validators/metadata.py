from pydantic import BaseModel

class MetaData(BaseModel):
    tool_id: int
    metadata: dict
    score:float