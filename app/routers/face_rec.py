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

# import lecture service

from services.lectures import lectureServices

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
	try:
		# get the lecture images and student encodings from the database

		# get all lecture images in between the start and end time
		# instantiate lecture
		lecture_obj = lectureServices()
		print(class_att.start_time, class_att.end_time)
		print(class_att.panel_id)
		# print(class_att.lecture_id)
		lecture_images = lecture_obj.get_lecture_images_between_time(class_att.start_time,class_att.end_time)

		# get all encodings of students in the panel
		student_encodings = lecture_obj.get_student_encodings_from_panel_id(class_att.panel_id)

		student_ids = lecture_obj.get_student_ids_from_panel_id(class_att.panel_id)

		# check encoding id is present for each student
		# if not present, return error
		# if present, add to the list of student encodings

		print("lecture images ", lecture_images)
		print("student encodings ", student_encodings)
		print("student ids ", student_ids)

		# face_rec_obj = FaceRec(lecture_images,student_encodings,class_att.panel_id,student_ids)

		# add new row to classes collection

		lecture_obj.add_lecture(class_att)
	except Exception as e:
		print("An error occurred:", str(e))

	pass
	
