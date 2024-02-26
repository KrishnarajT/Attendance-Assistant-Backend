# Main Class file for FaceRecognition
# import face_recognition
import threading


class FaceRec:
	"""
		Contains methods for facial recognition of multiple students, being present in a single image. So basically if you wanna get the attendance of a class, you have to instantiate this class, and then call the methods to get the attendance. It contains all the methods that will actually perform the facial recognition using multithreading. After you are done you can simply delete the object, and all the data will be cleaned up.
	"""

	def __init__(self):
		"""
			Constructor
		"""
		print("Beginning Face Recognition!")

	def cleanup(self):
		"""
			Cleanup all data from memory.
		"""
		pass

	def create_encodings_for_test_img(self):
		"""
			create encodings for all images in the Image that we have to test for faces.
		"""
		pass
