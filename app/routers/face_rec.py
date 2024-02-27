'''
This file contains the routes for interaction with any face recognition models, or actually carrying out the face recognition process.
'''

# import fastapi stuff
from fastapi import APIRouter

# import face rec stuff
from facial_recognition.FaceRec import FaceRec  # main class

# import db stuff
from services.assistanceMongoDB import MongoService
# import models
from models.ClientUploadModels import AttendanceModel
from models.StudentModels import EncodingModel
router = APIRouter(prefix="/face_rec", tags=["Face Recognition"])


@router.get("/test", status_code=200, summary="Test route")
def index():
	test_obj = FaceRec()
	# so ideally objects of this class would receive encodings of all the students, and the class image. We would get
	# this from calling functions of other routes (like getting student urls, encoding urls, etc), and then we would
	# call the methods of this class to get the attendance. we would then return that attendance.
	return "Hello, World!"


@router.post("/add_attendance", status_code=200, summary="add attendace")
def get_attendance(class_att: AttendanceModel):
	"""
	Add attendance to the database.

	:param class_att: The attendance model.

	:return: The attendance model.
	"""
	# get the lecture images and student encodings from the database

	#get all lecture images in between the start and end time

	mongo_obj = MongoService()
	
	lecture_images = mongo_obj.get_lecture_images_between_time(class_att.start_time, class_att.end_time)

	# get all encodings of students in the panel
	student_encodings = mongo_obj.get_student_encodings_from_panel_id(class_att.panel_id)
	# instantiate the face rec object
	face_rec_obj = FaceRec(lecture_images,student_encodings,panel_id,student_ids)

	# add new row to classes collection
	pass
	
