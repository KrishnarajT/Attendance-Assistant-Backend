from data.mongodb import connect_to_mongo
from bson.objectid import ObjectId
from pymongo.errors import PyMongoError

# refer to this names only. while doing any operation on the database
# collection names: buildings, rooms, subjects, teachers, students, semesters ,specializations, panels, lectureImages, encodings, schools


class MongoService:
    def __init__(self):
        self.db = connect_to_mongo()

    def add_teacher(self, teacher):
        try:
            self.db["teachers"].insert_one(teacher.dict())
            return teacher
        except Exception as e:
            print(f"An error occurred while inserting the teacher: {e}")
            return None

    def add_subject(self, subject):
        try:
            self.db["subjects"].insert_one(subject.dict())
            return subject
        except Exception as e:
            print(f"An error occurred while inserting the subject: {e}")
            return None

    def get_all_teachers(self):
        try:
            teachers = self.db["teachers"].find()
            return [
                {
                    "_id": str(teacher["_id"]),
                    **{key: value for key, value in teacher.items() if key != "_id"},
                }
                for teacher in teachers
            ]

        except Exception as e:
            print(f"An error occurred while getting all teachers: {e}")
            return None

    def get_all_subjects(self):
        try:
            subjects = self.db["subjects"].find()
            return [
                {
                    "_id": str(subject["_id"]),
                    **{key: value for key, value in subject.items() if key != "_id"},
                }
                for subject in subjects
            ]
        except Exception as e:
            print(f"An error occurred while getting all subjects: {e}")
            return None

    def add_panel(self, panel):
        try:
            self.db["panels"].insert_one(panel.dict())
            return panel
        except Exception as e:
            print(f"An error occurred while inserting the panel: {e}")
            return None

    def get_all_panels(self):
        try:
            panels = self.db["panels"].find()
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

    def get_teacher_by_id(self, teacher_id):
        try:
            teacher = self.db["teachers"].find_one({"_id": ObjectId(teacher_id)})
            if teacher:
                return {
                    "_id": str(teacher["_id"]),
                    **{key: value for key, value in teacher.items() if key != "_id"},
                }
            else:
                return None
        except Exception as e:
            print(f"An error occurred while getting the teacher: {e}")
            return None

    def get_student_by_panel_id(self, panel_id):
        try:
            student_ids_from_panel = self.db["panels"].find_one(
                {"_id": ObjectId(panel_id)}
            )["students"]
            # get the student row from the students collection using the ids we retrieved
            students = {}
            for student_id in student_ids_from_panel:
                student = self.db["students"].find_one({"_id": ObjectId(student_id)})
                if student:
                    students[str(student["_id"])] = {
                        key: value for key, value in student.items() if key != "_id"
                    }
            return students

        except Exception as e:
            print(f"An error occurred while getting the students: {e}")
            return None

    def get_student_encoding_from_student_id(self, student_id):
        """Gets the student encoding dictionary that is stored in mongodb. 

        Args:
            student_id (string): the id of the student that we want the encoding from. 

        Returns:
            dictionary: the encoding of the student. 
        """
        try:
            # getting the student encoding id from students collection
            student = self.db["students"].find_one({"_id": ObjectId(student_id)})
            encoding_id = student["face_encoding"]
            # get the encoding url from the encodings collection as a string
            encoding = self.db["encodings"].find_one({"_id": ObjectId(encoding_id)})
            return encoding
        except Exception as e:
            print(f"An error occurred while getting the student encoding: {e}")
            return None

    def add_student_face_to_db(self, student_id, face_url):
        """Adds the face url to the faces list of the student row matching with id = student_id. 

        Args:
            student_id (str): id of the student that you wanna add the face of. 
            face_url (str): url of the firebase storage of the image containing the face of the concerned student. 
        """
        try:
            self.db["students"].update_one(
                {"_id": ObjectId(student_id)}, {"$push": {"faces": face_url}}
            )
        except Exception as e:
            print(f"An error occurred while adding the face to the student: {e}")

    def get_all_students(self):
        try:
            students = self.db["students"].find()
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

    def add_student(self, student):
        try:
            mongo_output = self.db["students"].insert_one(student.dict())
            student.set_id(str(mongo_output.inserted_id))
            return student
        except Exception as e:
            print(f"An error occurred while inserting the student: {e}")
            return None

    def add_class_photo_to_db(self, room_id, date, time, class_photo_url):
        try:
            self.db["lectureImages"].insert_one(
                {
                    "room_id": room_id,
                    "date": date,
                    "time": time,
                    "class_photo_url": class_photo_url,
                }
            )
        except Exception as e:
            print(f"An error occurred while inserting the class photo: {e}")

    def get_all_class_photos(self):
        try:
            class_photos = self.db["lectureImages"].find()
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

    def get_all_rooms(self):
        try:
            rooms = self.db["rooms"].find()
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

    def add_room(self, room):
        try:
            mongo_output = self.db["rooms"].insert_one(room.dict())
            room.set_id(str(mongo_output.inserted_id))
            return room
        except Exception as e:
            print(f"An error occurred while inserting the room: {e}")
            return None

    def add_building(self, building):
        try:
            mongo_output = self.db["buildings"].insert_one(building.dict())
            building.set_id(str(mongo_output.inserted_id))
            return building
        except Exception as e:
            print(f"An error occurred while inserting the building: {e}")
            return None

    def get_all_buildings(self):
        try:
            buildings = self.db["buildings"].find()
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

    def get_rooms_from_building_id(self, building_id):
        try:
            rooms = self.db["rooms"].find({"building_id": ObjectId(building_id)})
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

    def add_room_to_building(self, room_id, building_id):
        try:
            self.db["buildings"].update_one(
                {"_id": ObjectId(building_id)}, {"$push": {"rooms": room_id}}
            )
        except Exception as e:
            print(f"An error occurred while adding the room to the building: {e}")

    def add_panel(self, panel):
        try:
            mongo_output = self.db["panels"].insert_one(panel.dict())
            panel.set_id(str(mongo_output.inserted_id))
            return panel
        except Exception as e:
            print(f"An error occurred while inserting the panel: {e}")
            return None

    def add_school(self, school):
        try:
            mongo_output = self.db["schools"].insert_one(school.dict())
            school.set_id(str(mongo_output.inserted_id))
            return school
        except Exception as e:
            print(f"An error occurred while inserting the school: {e}")
            return None

    def get_all_schools(self):
        try:
            schools = self.db["schools"].find()
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

    def add_specialization(self, specialization):
        try:
            mongo_output = self.db["specializations"].insert_one(specialization.dict())
            specialization.set_id(str(mongo_output.inserted_id))
            return specialization
        except Exception as e:
            print(f"An error occurred while inserting the specialization: {e}")
            return None

    def get_all_specializations(self):
        try:
            specializations = self.db["specializations"].find()
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

    def add_spec_to_school(self, school_id, spec_id):
        try:
            self.db["schools"].update_one(
                {"_id": ObjectId(school_id)}, {"$push": {"specializations": ObjectId(spec_id)}}
            )
        except Exception as e:
            print(f"An error occurred while adding the specialization to the school: {e}")

    def update_school_for_panel(self, panel_id, school_id):
        try:
            self.db["panels"].update_one(
                {"_id": ObjectId(panel_id)}, {"$set": {"school_id": ObjectId(school_id)}}
            )
        except Exception as e:
            print(f"An error occurred while updating the school for the panel: {e}")

    def update_spec_for_panel(self, panel_id, spec_id):
        try:
            self.db["panels"].update_one(
                {"_id": ObjectId(panel_id)}, {"$set": {"spec_id": ObjectId(spec_id)}}
            )
        except Exception as e:
            print(f"An error occurred while updating the specialization for the panel: {e}")

    def set_current_sem_for_panel(self, panel_id, sem_id):
        try:
            self.db["panels"].update_one(
                {"_id": ObjectId(panel_id)}, {"$set": {"current_sem": ObjectId(sem_id)}}
            )
        except Exception as e:
            print(f"An error occurred while setting the current semester for the panel: {e}")

    def add_semester_to_panel(self, panel_id, sem_id):
        try:
            self.db["panels"].update_one(
                {"_id": ObjectId(panel_id)}, {"$push": {"semesters": ObjectId(sem_id)}}
            )
        except Exception as e:
            print(f"An error occurred while adding the semester to the panel: {e}")

    def add_student_to_panel(self, panel_id, student_id):
        try:
            self.db["panels"].update_one(
                {"_id": ObjectId(panel_id)}, {"$push": {"students": student_id}}
            )
        except PyMongoError as e:
            print(e)
            print(f"An error occurred while adding the student to the panel: {e}")
            return False
        return True