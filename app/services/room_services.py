from data.mongodb import connect_to_mongo
from bson import ObjectId
from pymongo.errors import PyMongoError
db = connect_to_mongo()


def get_all_rooms():
    try:
        rooms = db["rooms"].find()
        return [
            {
                "_id": str(room["_id"]),
                **{key: value for key, value in room.items() if key != "_id"},
            }
            for room in rooms
        ]
    except Exception as e:
        print(f"An error occurred while getting all rooms: {e}")
        return None


def add_room(room):
    try:
        mongo_output = db["rooms"].insert_one(room.dict())
        room.set_id(str(mongo_output.inserted_id))
        return room
    except Exception as e:
        print(f"An error occurred while inserting the room: {e}")
        return None


def add_building(building):
    try:
        mongo_output = db["buildings"].insert_one(building.dict())
        building.set_id(str(mongo_output.inserted_id))
        return building
    except Exception as e:
        print(f"An error occurred while inserting the building: {e}")
        return None


def get_all_buildings():
    try:
        buildings = db["buildings"].find()
        return [
            {
                "_id": str(building["_id"]),
                **{key: value for key, value in building.items() if key != "_id"},
            }
            for building in buildings
        ]
    except Exception as e:
        print(f"An error occurred while getting all buildings: {e}")
        return None


def get_rooms_from_building_id(building_id):
    try:
        rooms = db["rooms"].find({"building_id": ObjectId(building_id)})
        return [
            {
                "_id": str(room["_id"]),
                **{key: value for key, value in room.items() if key != "_id"},
            }
            for room in rooms
        ]
    except Exception as e:
        print(f"An error occurred while getting the rooms: {e}")
        return None


def add_room_to_building(room_id, building_id):
    try:
        db["buildings"].update_one(
            {"_id": ObjectId(building_id)}, {"$push": {"rooms": room_id}}
        )
    except Exception as e:
        print(f"An error occurred while adding the room to the building: {e}")
