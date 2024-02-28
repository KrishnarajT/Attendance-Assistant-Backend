"""
This contains Class and function for adding and getting lectures from the database.
"""


from services.assistanceMongoDB import MongoService


class lectureServices:

    def add_lecture(lecture_details):
        """
        Add a lecture to the database.
        """
        # add the lecture to the database
        try:
            # instantiate the mongo service
            mongo_obj = MongoService()
            # call the function from mongo service to add the lecture
            lecture_response = mongo_obj.add_lecture(lecture_details)
            return lecture_response
        except Exception as e:
            # handle exception
            pass

    def get_lecture(lecture_id):
        """
        Get a lecture from the database.
        """
        # get the lecture from the database
        try:
            # instantiate the mongo service
            mongo_obj = MongoService()
            # call the function from mongo service to get the lecture
            lecture_response = mongo_obj.get_lecture(lecture_id.lec_id)
            return lecture_response
        except Exception as e:
            # handle exception
            pass

    def get_all_lectures():
        """
        Get all lectures from the database.
        """
        # get all the lectures from the database
        try:
            # instantiate the mongo service
            mongo_obj = MongoService()
            # call the function from mongo service to get all the lectures
            lecture_response = mongo_obj.get_all_lectures()
            return lecture_response
        except Exception as e:
            # handle exception
            pass
    
    def get_lecture_images_between_time(start_time,end_time):
        """
        Get all lecture images between a start and end time.
        """
        # get all the lecture images between the start and end time
        try:
            # instantiate the mongo service
            mongo_obj = MongoService()
            # call the function from mongo service to get all the lecture images between the start and end time
            lecture_images = mongo_obj.get_lecture_images_between_time(start_time, end_time)
            return lecture_images
        except Exception as e:
            # handle exception
            
            pass

    def get_student_encodings_from_panel_id(panel_id):
        """
        Get all student encodings from a panel id.
        """
        # get all the student encodings from a panel id
        try:
            # instantiate the mongo service
            mongo_obj = MongoService()
            # call the function from mongo service to get all the student encodings from a panel id
            student_encodings = mongo_obj.get_student_encodings_from_panel_id(panel_id)
            return student_encodings
        except Exception as e:
            # handle exception
            pass
    def get_student_ids_from_panel_id(panel_id):
        """
        Get all student ids from a panel id.
        """
        # get all the student ids from a panel id
        try:
            # instantiate the mongo service
            mongo_obj = MongoService()
            # call the function from mongo service to get all the student ids from a panel id
            student_ids = mongo_obj.get_student_ids_from_panel_id(panel_id)
            return student_ids
        except Exception as e:
            # handle exception
            pass
    
    