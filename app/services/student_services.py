from data.mongodb import connect_to_mongo
from bson import ObjectId
db = connect_to_mongo()


def get_student_encoding_from_student_id(student_id):
    """Gets the student encoding dictionary that is stored in mongodb.

    Args:
        student_id (string): the id of the student that we want the encoding from.

    Returns:
        dictionary: the encoding of the student.
    """
    try:
        # getting the student encoding id from students collection
        student = db["students"].find_one({"_id": ObjectId(student_id)})
        encoding_id = student["face_encoding"]
        # get the encoding url from the encodings collection as a string
        encoding = db["encodings"].find_one({"_id": ObjectId(encoding_id)})
        return encoding
    except Exception as e:
        print(f"An error occurred while getting the student encoding: {e}")
        return None


def add_student_face_to_db(student_id, face_url):
    """Adds the face url to the faces list of the student row matching with id = student_id.

    Args:
        student_id (str): id of the student that you wanna add the face of.
        face_url (str): url of the firebase storage of the image containing the face of the concerned student.
    """
    try:
        db["students"].update_one(
            {"_id": ObjectId(student_id)}, {"$push": {"faces": face_url}}
        )
    except Exception as e:
        print(f"An error occurred while adding the face to the student: {e}")


def get_all_students():
    try:
        students = db["students"].find()
        return [
            {
                "_id": str(student["_id"]),
                **{key: value for key, value in student.items() if key != "_id"},
            }
            for student in students
        ]
    except Exception as e:
        print(f"An error occurred while getting all students: {e}")
        return None


def add_student(student):
    try:
        mongo_output = db["students"].insert_one(student.dict())
        student.set_id(str(mongo_output.inserted_id))
        return student
    except Exception as e:
        print(f"An error occurred while inserting the student: {e}")
        return None


def add_student_encoding(student_id, encoding):
    try:
        mongo_output = db["encodings"].insert_one(encoding)
        encoding_id = str(mongo_output.inserted_id)
        db["students"].update_one(
            {"_id": ObjectId(student_id)}, {"$set": {"face_encoding": encoding_id}}
        )
        return encoding_id
    except Exception as e:
        print(f"An error occurred while adding the student encoding: {e}")


def get_student_encodings_from_student_ids(student_ids):
    """
    Get all student encodings from the panel id.
    :param panel_id: The panel id.
    :return: The student encodings.
    """
    try:
        student_encodings = {}
        for student_id in student_ids:
            student = db["students"].find_one({"_id": ObjectId(student_id)})
            # check if their faces are present
            if len(student["faces"]) == 0:
                raise Exception(f"Student {student_id} has no faces")
            student_encodings[str(student["_id"])] = student["face_encoding"]
        return student_encodings
    except Exception as e:
        print(f"An error occurred while getting the student encodings: {e}")
        return None
