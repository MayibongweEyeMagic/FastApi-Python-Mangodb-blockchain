from pydantic import BaseModel
import datetime as _dt

class Block(BaseModel):
    index:int
    Timestamp:str
    data: str
    proof:int
    Previous_hash:str
    
