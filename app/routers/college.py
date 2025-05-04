"""
This includes routes for getting and setting data about rooms and buildings.
"""

# import fastapi stuff
from fastapi import APIRouter, Response, HTTPException

# importing db
from pymongo.errors import PyMongoError
from services.room_services import (
    get_all_rooms,
    add_room,
    add_building,
    get_all_buildings,
    get_rooms_from_building_id,
    add_room_to_building,
)

# importing models
from models.CollegeModels import (
    RoomModel,
    BuildingModel,
    RoomResponseModel,
    BuildingResponseModel,
)


router = APIRouter(prefix="/college", tags=["Rooms and Buildings"])


@router.get("/test", status_code=200, summary="Test route")
def index_route():
    return Response(content="Hello, World!", status_code=200)


@router.get("/get_all_rooms", status_code=200, summary="Get all rooms")
def get_all_rooms_from_db_route():
    """
    This route gets all the rooms from the database.
    : return: A list of all the rooms in the database.
    """
    try:
        rooms = get_all_rooms()
        if rooms:
            return rooms
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while adding the panel"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/add_room", status_code=201, summary="Add a room")
def add_room_route(roomModel: RoomModel):
    """
    This route adds a room to the database.
    : param room: The room to be added.
    : return: The added room.
    """
    try:
        room = add_room(roomModel)
        if not room:
            raise HTTPException(
                status_code=500, detail="An error occurred while adding the panel"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return RoomResponseModel(
        name=room.name,
        room_id=room._id,
    )


@router.post("/add_building", status_code=201, summary="Add a building")
def add_building_route(buildingModel: BuildingModel):
    """
    This route adds a building to the database.
    : param building: The building to be added.
    : return: The added building.
    """
    try:
        building = add_building(buildingModel)
        print(building)
        if not building:
            raise HTTPException(
                status_code=500, detail="An error occurred while adding the panel"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))

    return BuildingResponseModel(
        name=building.name,
        building_id=building._id,
        rooms=building.rooms,
    )


@router.get("/get_all_buildings", status_code=200, summary="Get all buildings")
def get_all_buildings_route():
    """
    This route gets all the buildings from the database.
    : return: A list of all the buildings in the database.
    """
    try:
        all_buildings = get_all_buildings()
        if all_buildings:
            return all_buildings
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while adding the panel"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/get_rooms_from_building_id", status_code=200, summary="Get rooms from building id"
)
def get_rooms_from_building_id_route(building_id: str):
    """
    This route gets all the rooms from the database.
    : return: A list of all the rooms in the database.
    """
    try:
        rooms = get_rooms_from_building_id(building_id)
        if rooms:
            return rooms
        else:
            raise HTTPException(
                status_code=500, detail="An error occurred while adding the panel"
            )
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/add_room_to_building", status_code=201, summary="Add a room to a building"
)
def add_room_to_building_route(room_id: str, building_id: str):
    """
    This route adds a room to a building.
    : param room_id: The room id to be added.
    : param building_id: The building id to be added.
    : return: The added room to the building.
    """
    try:
        add_room_to_building(room_id, building_id)
        return True
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
