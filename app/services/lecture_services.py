"""
This contains Class and function for adding and getting lectures from the database.
"""

from data.mongodb import connect_to_mongo
from bson import ObjectId

db = connect_to_mongo()


def add_class_photo_to_db(room_id, date, time, class_photo_url):
    try:
        db["lectureImages"].insert_one(
            {
                "room_id": room_id,
                "date": date,
                "time": time,
                "class_photo_url": class_photo_url,
            }
        )
    except Exception as e:
        print(f"An error occurred while inserting the class photo: {e}")


def get_all_class_photos():
    try:
        class_photos = db["lectureImages"].find()
        return [
            {
                "_id": str(class_photo["_id"]),
                **{key: value for key, value in class_photo.items() if key != "_id"},
            }
            for class_photo in class_photos
        ]
    except Exception as e:
        print(f"An error occurred while getting all class photos: {e}")
        return None


def add_lecture(lecture):
    try:
        mongo_obj = db["classes"].insert_one(lecture)
        return str(mongo_obj.inserted_id)
    except Exception as e:
        print(f"An error occurred while adding the lecture: {e}")
        return False


def get_lecture(lecture_id):
    try:
        lecture = db["classes"].find_one({"_id": ObjectId(lecture_id)})
        return {
            "_id": str(lecture["_id"]),
            **{key: value for key, value in lecture.items() if key != "_id"},
        }
    except Exception as e:
        print(f"An error occurred while getting the lecture: {e}")
        return None


def get_all_lectures():
    try:
        lectures = db["classes"].find()
        return [
            {
                "_id": str(lecture["_id"]),
                **{key: value for key, value in lecture.items() if key != "_id"},
            }
            for lecture in lectures
        ]
    except Exception as e:
        print(f"An error occurred while getting all lectures: {e}")
        return None


def get_lecture_images_between_time_on_date(start_time, end_time, given_date):
    try:
        lecture_images = db["lectureImages"].find(
            {
                "time": {"$gte": start_time, "$lte": end_time},
                "date": given_date,
            }
        )
        # return the class_photo_url attribute of each row of the lectureimages that we found
        lecs = []
        for lecture_image in lecture_images:
            lecs.append(str(lecture_image["class_photo_url"]))
        return lecs
    except Exception as e:
        print(f"An error occurred while getting the lecture images: {e}")
        return None
