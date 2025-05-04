from pydantic import BaseModel
from typing import Optional, List


class RoomModel(BaseModel):
    name: str

    def set_id(self, _id):
        self._id = _id


class RoomResponseModel(BaseModel):
    name: str
    room_id: str


class BuildingModel(BaseModel):
    name: str
    rooms: Optional[List] = []

    def set_id(self, _id):
        self._id = _id


class BuildingResponseModel(BaseModel):
    name: str
    building_id: str
    rooms: Optional[List] = []
