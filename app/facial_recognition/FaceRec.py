# Main Class file for FaceRecognition
import face_recognition
import threading
from routers.client_uploads import add_face_encoding
import pickle


class FaceRec:
	"""
	Contains methods for facial recognition of multiple students, being present in a single image. So basically if you
	wanna get the attendance of a class, you have to instantiate this class, and then call the methods to get the
	attendance. It contains all the methods that will actually perform the facial recognition using multithreading.
	After you are done you can simply delete the object, and all the data will be cleaned up.
	"""

	def __init__(self, student_face_encodings: dict, class_images: list, panel_id: str, student_ids: list):
		"""
		:param student_face_encodings: dictionary containing the face encodings of the students. The keys are the
		student ids, and the values are the face encodings of the students.

		"""
		if student_face_encodings is None:
			student_face_encodings = {}
		print("Init Face Recognition!")
		self.student_face_encodings = student_face_encodings
		self.class_images = []
		self.panel_id = panel_id
		self.students_present = []
		self.students_absent = []
		self.student_ids = student_ids

	def find_attendance(self):
		"""
		Perform the facial recognition on the class images, and return the attendance.
		"""
		# create threads for each image
		threads = []
		for image in self.class_images:
			t = threading.Thread(target=self.recognize_faces, args=(image,))
			threads.append(t)
			t.start()

		# wait for all threads to finish
		for t in threads:
			t.join()

		# filter the students_present list to remove duplicates
		self.students_present = list(set(self.students_present))
		# get absent students
		self.students_absent = list(set(self.student_ids) - set(self.students_present))
		return self.students_present, self.students_absent

	def recognize_faces(self, image):
		"""
		Recognize the faces in the given image, and update the attendance.
		"""
		# load the image
		image = face_recognition.load_image_file(image)

		# get the face locations
		face_locations = face_recognition.face_locations(image)

		# get the face encodings
		face_encodings = face_recognition.face_encodings(image, face_locations)

		# check if the face encodings match with the students' face encodings
		for face_encoding in face_encodings:
			# compare the face encodings
			matches = face_recognition.compare_faces(list(self.student_face_encodings.values()), face_encoding)

			# get the student id
			student_id = list(self.student_face_encodings.keys())[matches.index(True)]

			# add the student to the present list
			self.students_present.append(student_id)

	def add_student_face_encodings(self, student_id, student_face_encodings):
		"""
		Add the face encodings of the student to the class face encodings.
		"""
		self.student_face_encodings[student_id] = student_face_encodings

	def add_class_images(self, class_images):
		"""
		Add the class images to the class images list.
		"""
		self.class_images.append(class_images)

	# clean up
	def __del__(self):
		"""
		Clean up the object.
		"""
		print("Cleaning up Face Recognition!")
		del self.student_face_encodings
		del self.class_images
		del self.students_present
		del self.students_absent
		del self.student_ids
		del self.panel_id

	# getter methods
	def get_students_present(self):
		"""
		Get the students present in the class.
		"""
		return self.students_present

	def get_students_absent(self):
		"""
		Get the students absent in the class.
		"""
		return self.students_absent

	def get_student_face_encodings(self):
		"""
		Get the student face encodings.
		"""
		return self.student_face_encodings

	def get_class_images(self):
		"""
		Get the class images.
		"""
		return self.class_images

	def get_panel_id(self):
		"""
		Get the panel id.
		"""
		return self.panel_id

	def get_student_ids(self):
		"""
		Get the student ids.
		"""
		return self.student_ids

	# setter methods
	def set_students_present(self, students_present):
		"""
		Set the students present in the class.
		"""
		self.students_present = students_present

	def set_students_absent(self, students_absent):
		"""
		Set the students absent in the class.
		"""
		self.students_absent = students_absent

	def set_student_face_encodings(self, student_face_encodings):
		"""
		Set the student face encodings.
		"""
		self.student_face_encodings = student_face_encodings

	def set_class_images(self, class_images):
		"""
		Set the class images.
		"""
		self.class_images = class_images

	def set_panel_id(self, panel_id):
		"""
		Set the panel id.
		"""
		self.panel_id = panel_id

	def set_student_ids(self, student_ids):
		"""
		Set the student ids.
		"""
		self.student_ids = student_ids
