from pydantic import BaseModel
from typing import Optional, List

class RoomModel(BaseModel):
    name: str
    
class BuildingModel(BaseModel):
    name: str
    rooms: Optional[List] = []