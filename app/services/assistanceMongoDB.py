from data.mongodb import connect_to_mongo

#refer to this names only. while doing any operation on the database
#collection names: buildings, rooms, subjects, teachers, students, semesters ,specializations, panels, lectureImages, encodings, schools

class AssistanceService:
    def __init__(self):
        self.db = connect_to_mongo()


    def add_teacher(self, teacher):
        try:
            self.db['teachers'].insert_one(teacher.dict())
            return teacher
        except Exception as e:
            print(f"An error occurred while inserting the teacher: {e}")
            return None
        
    def add_subject(self, subject):
        try:
            self.db['subjects'].insert_one(subject.dict())
            return subject
        except Exception as e:
            print(f"An error occurred while inserting the subject: {e}")
            return None
    
    def get_all_teachers(self):
        try:
            teachers = self.db['teachers'].find()
            return [{'_id': str(teacher['_id']), **{key: value for key, value in teacher.items() if key != '_id'}} for teacher in teachers]

        except Exception as e:
            print(f"An error occurred while getting all teachers: {e}")
            return None
        
    def get_all_subjects(self):
        try:
            subjects = self.db['subjects'].find()
            return [{'_id': str(subject['_id']), **{key: value for key, value in subject.items() if key != '_id'}} for subject in subjects]
        except Exception as e:
            print(f"An error occurred while getting all subjects: {e}")
            return None
    
    def add_panel(self, panel):
        try:
            self.db['panels'].insert_one(panel.dict())
            return panel
        except Exception as e:
            print(f"An error occurred while inserting the panel: {e}")
            return None
    
    def get_all_panels(self):
        try:
            panels = self.db['panels'].find()
            return [{'_id': str(panel['_id']), **{key: value for key, value in panel.items() if key != '_id'}} for panel in panels]
        except Exception as e:
            print(f"An error occurred while getting all panels: {e}")
            return None
        
    def get_teacher_by_id(self, teacher_id):
        try:
            teacher = self.db['teachers'].find_one({"_id": teacher_id})
            if teacher:
                return {'_id': str(teacher['_id']), **{key: value for key, value in teacher.items() if key != '_id'}}
            else:
                return None
        except Exception as e:
            print(f"An error occurred while getting the teacher: {e}")
            return None