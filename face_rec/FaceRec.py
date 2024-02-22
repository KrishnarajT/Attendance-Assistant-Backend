# Main Class file for FaceRecognition
import face_recognition
import threading

class FaceRec:
	"""
		Contains methods for facial recognition
	"""

	def __init__(self, test_image_uri, ):
		"""
			Constructor
		"""
		self.test_image_uri = test_image_uri


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
