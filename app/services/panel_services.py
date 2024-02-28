from data.mongodb import connect_to_mongo
from bson import ObjectId
from pymongo.errors import PyMongoError

db = connect_to_mongo()

import services.panel_services
from services.student_services import (
    get_student_encodings_from_student_ids,
)

def get_student_encodings_from_panel_id(panel_id):
    """
    Get all student encodings from a panel id.
    """
    # get all the student encodings from a panel id
    try:
        # get all students in a panel.
        student_ids = get_student_ids_from_panel_id(panel_id)
        print(student_ids, "are the students that are present in the panel ", panel_id)
        student_encodings, student_faces, no_faces = get_student_encodings_from_student_ids(student_ids)
        if len(no_faces) > 0:
            print("These students do not have faces: ", no_faces)
        return student_encodings, no_faces
    except Exception as e:
        # handle exception
        print(e)
        raise e


def add_panel(panel):
    try:
        db["panels"].insert_one(panel.dict())
        return panel
    except Exception as e:
        print(f"An error occurred while inserting the panel: {e}")
        return None


def get_all_panels():
    try:
        panels = db["panels"].find()
        panels = [
            {
                "_id": str(panel["_id"]),
                **{key: value for key, value in panel.items() if key != "_id"},
            }
            for panel in panels
        ]
        print(panels)
        return panels
    except Exception as e:
        print(f"An error occurred while getting all panels: {e}")
        return None


def get_student_by_panel_id(panel_id):
    try:
        student_ids_from_panel = db["panels"].find_one({"_id": ObjectId(panel_id)})[
            "students"
        ]
        # get the student row from the students collection using the ids we retrieved
        students = {}
        for student_id in student_ids_from_panel:
            student = db["students"].find_one({"_id": ObjectId(student_id)})
            if student:
                students[str(student["_id"])] = {
                    key: value for key, value in student.items() if key != "_id"
                }
        return students

    except Exception as e:
        print(f"An error occurred while getting the students: {e}")
        return None


def add_panel(panel):
    try:
        mongo_output = db["panels"].insert_one(panel.dict())
        panel.set_id(str(mongo_output.inserted_id))
        return panel
    except Exception as e:
        print(f"An error occurred while inserting the panel: {e}")
        return None


def set_current_sem_for_panel(panel_id, sem_id):
    try:
        db["panels"].update_one(
            {"_id": ObjectId(panel_id)}, {"$set": {"current_sem": ObjectId(sem_id)}}
        )
    except Exception as e:
        print(
            f"An error occurred while setting the current semester for the panel: {e}"
        )


def add_semester_to_panel(panel_id, sem_id):
    try:
        db["panels"].update_one(
            {"_id": ObjectId(panel_id)}, {"$push": {"semesters": ObjectId(sem_id)}}
        )
    except Exception as e:
        print(f"An error occurred while adding the semester to the panel: {e}")

def add_semester(semester):
    try:
        mongo_output = db["semesters"].insert_one(semester.dict())
        semester.set_id(str(mongo_output.inserted_id))
        return semester
    except Exception as e:
        print(f"An error occurred while inserting the semester: {e}")
        return None


def add_student_to_panel(panel_id, student_id):
    try:
        db["panels"].update_one(
            {"_id": ObjectId(panel_id)}, {"$push": {"students": student_id}}
        )
    except PyMongoError as e:
        print(e)
        print(f"An error occurred while adding the student to the panel: {e}")
        return False
    return True


def get_all_semesters():
    try:
        semesters = db["semesters"].find()
        return [
            {
                "_id": str(semester["_id"]),
                **{key: value for key, value in semester.items() if key != "_id"},
            }
            for semester in semesters
        ]
    except Exception as e:
        print(f"An error occurred while getting all semesters: {e}")
        return None


def get_student_ids_from_panel_id(panel_id):
    try:
        student_ids = db["panels"].find_one({"_id": ObjectId(panel_id)})["students"]
        return student_ids
    except Exception as e:
        print(f"An error occurred while getting the student ids: {e}")
        return None
