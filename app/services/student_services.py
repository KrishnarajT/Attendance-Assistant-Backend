from data.mongodb import connect_to_mongo
from bson import ObjectId
from services.assistanceFirebase import AssistanceFirebase

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


async def add_student_encoding(student_id, number_of_faces, encoding):
    """uploads the student encoding, and puts it in the students collection as well as the encoding collection.

    Args:
        student_id (str): id of the student whose encoding is to be added.
        encoding (pkl): pkl serialized object.

    Returns:
        True if done well, else False
    """
    print(
        "encoding in the add student encoding function in student services is ",
        encoding,
    )
    # add encoding to firebase.
    assist_firebase = AssistanceFirebase()
    assist_firebase.upload_encoding(encoding)
    encoding_url = assist_firebase.get_encoding_url()
    encoding = {
        "student": student_id,
        "encoding": encoding_url,
        "number_of_faces": number_of_faces,
    }

    try:
        # add encoding to the encodings collection
        mongo_output = db["encodings"].insert_one(encoding)
        encoding_id = str(mongo_output.inserted_id)

        # add encoding id to the student row
        db["students"].update_one(
            {"_id": ObjectId(student_id)}, {"$set": {"face_encoding": encoding_id}}
        )
        return encoding_url
    except Exception as e:
        print(f"An error occurred while adding the student encoding: {e}")


def get_student_encodings_from_student_ids(student_ids):
    """
    Get all student encodings from the panel id.
    :param panel_id: The panel id.
    :return: The student encodings.
    """
    try:
        print("trying to get student encodings")
        student_encodings = {}
        no_faces = []
        student_faces = {}
        for student_id in student_ids:
            print(student_id)
            student = db["students"].find_one({"_id": ObjectId(student_id)})
            print(student)
            # check if their faces are present
            if len(student["faces"]) == 0:
                no_faces.append(student_id)
            else:
                student_faces[str(student["_id"])] = student["faces"]
            student_encodings[str(student["_id"])] = get_encoding_url_from_id(
                student["face_encoding"]
            )

        return (student_encodings, student_faces, no_faces)
    except Exception as e:
        print(f"An error occurred while getting the student encodings: {e}")
        return e


def get_encoding_url_from_id(encoding_id):
    """
    Get the encoding url from the encoding id.
    :param encoding_id: The encoding id.
    :return: The encoding url.
    """
    try:
        encoding = db["encodings"].find_one({"_id": ObjectId(encoding_id)})
        return encoding["encoding"]
    except Exception as e:
        print(f"An error occurred while getting the encoding url: {e}")
        return None


def get_student_from_id(student_id):
    """
    Get the student from the id.
    :param student_id: The student id.
    :return: The student.
    """
    try:
        student = db["students"].find_one({"_id": ObjectId(student_id)})
        return student
    except Exception as e:
        print(f"An error occurred while getting the student: {e}")
        return None
