from data.mongodb import connect_to_mongo
from bson import ObjectId
from pymongo.errors import PyMongoError

db = connect_to_mongo()


def add_school(school):
    try:
        mongo_output = db["schools"].insert_one(school.dict())
        school.set_id(str(mongo_output.inserted_id))
        return school
    except Exception as e:
        print(f"An error occurred while inserting the school: {e}")
        return None


def get_all_schools():
    try:
        schools = db["schools"].find()
        return [
            {
                "_id": str(school["_id"]),
                **{key: value for key, value in school.items() if key != "_id"},
            }
            for school in schools
        ]
    except Exception as e:
        print(f"An error occurred while getting all schools: {e}")
        return None


def add_specialization(specialization):
    try:
        mongo_output = db["specializations"].insert_one(specialization.dict())
        specialization.set_id(str(mongo_output.inserted_id))
        return specialization
    except Exception as e:
        print(f"An error occurred while inserting the specialization: {e}")
        return None


def get_all_specializations():
    try:
        specializations = db["specializations"].find()
        return [
            {
                "_id": str(specialization["_id"]),
                **{key: value for key, value in specialization.items() if key != "_id"},
            }
            for specialization in specializations
        ]
    except Exception as e:
        print(f"An error occurred while getting all specializations: {e}")
        return None


def add_spec_to_school(school_id, spec_id):
    try:
        db["schools"].update_one(
            {"_id": ObjectId(school_id)},
            {"$push": {"specializations": ObjectId(spec_id)}},
        )
    except Exception as e:
        print(f"An error occurred while adding the specialization to the school: {e}")


def update_school_for_panel(panel_id, school_id):
    try:
        db["panels"].update_one(
            {"_id": ObjectId(panel_id)},
            {"$set": {"school_id": ObjectId(school_id)}},
        )
    except Exception as e:
        print(f"An error occurred while updating the school for the panel: {e}")


def update_spec_for_panel(panel_id, spec_id):
    try:
        db["panels"].update_one(
            {"_id": ObjectId(panel_id)}, {"$set": {"spec_id": ObjectId(spec_id)}}
        )
    except Exception as e:
        print(f"An error occurred while updating the specialization for the panel: {e}")
