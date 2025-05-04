"""
This class contains the methods that are related to creating and managing encodings of students' faces.
"""

# import the required libraries
import pickle
import face_recognition
import requests
import io
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


class StudentManager:

    def __init__(
        self,
        student_id: str,
        student_face_image_urls: list,
        student_face_encodings: list = [],
    ):
        """
        This class should be instantiated when we want to not actually perform any facial Recognition, but create
        encodings for the students, and update them to and from the dat abases. :param student_id: id of the student
        whose faces are provided in the images list :param student_face_image_urls: list of image urls that contain
        only one face, the face belonging to student with id 'student_id' :param student_face_encodings: list of face
        encodings of the student, note that these are not serialized, and are just the face encodings
        """
        print("Init Student Recognition Methods!")

        self.student_id = student_id
        self.student_face_encodings = student_face_encodings
        self.number_of_faces = 0
        self.serialized_student_face_encodings = None
        self.student_faces_image_urls = student_face_image_urls

    def create_face_encoding(self):
        """
        Create face encoding for the given image. Also create the serialized face encodings.
        images: list of image urls that contain only one face, the face belonging to student with id 'student_id'
        id: id of the student whose faces are provided in the images list
        """
        print("trying to create face encoding. ")
        self.number_of_faces = len(self.student_faces_image_urls)
        # Create face encoding for the given images
        for image in self.student_faces_image_urls:
            image_np = self.get_image_from_url(image)
            student_face_locations = face_recognition.face_locations(image_np)
            student_face_encoding = face_recognition.face_encodings(
                image_np, student_face_locations, num_jitters=10
            )[0]
            self.student_face_encodings.append(student_face_encoding)

        # serialize student_face_encodings so that we can upload it using pickle
        self.serialized_student_face_encodings = pickle.dumps(
            self.student_face_encodings
        )

    def get_image_from_url(self, image_url):
        print("now doing", image_url)
        response = requests.get(image_url)
        image_bytes = io.BytesIO(response.content)

        # Open the image with PIL so we can use it with face_recognition
        image = Image.open(image_bytes)

        # Convert the image to a numpy array so face_recognition can work with it
        image_np = np.array(image)

        return image_np

    def update_face_encoding(self, new_face_url):
        """
        Update the face encoding of the student with the new face.
        new_face: image url of the new face of the student
        student_id: id of the student whose face is to be updated
        """

        # load image file from the given url
        new_face_url = self.get_image_from_url(new_face_url)
        # Create face encoding for the given image
        new_student_image = face_recognition.face_locations(new_face_url)
        student_face_encoding = face_recognition.face_encodings(new_student_image)[0]

        # append to the list of face encodings
        self.student_face_encodings.append(student_face_encoding)

        # serialize student_face_encoding so that we can upload it using pickle
        self.serialized_student_face_encodings = pickle.dumps(
            self.student_face_encodings
        )
        return self.serialized_student_face_encodings

    def delete_face_encodings(self):
        """
        Delete the face encoding of the student with the given id.
        student_id: id of the student whose face is to be deleted
        """

        # clear all the face encodings
        self.student_face_encodings = []
        self.serialized_student_face_encodings = None

    # getter methods

    def get_student_id(self):
        """
        Get the student id.
        """
        return self.student_id

    def get_student_face_encodings(self):
        """
        Get the student face encodings.
        """
        return self.student_face_encodings

    def get_number_of_faces(self):
        """
        Get the number of faces.
        """
        return self.number_of_faces

    def get_serialized_student_face_encodings(self):
        """
        Get the serialized student face encodings.
        """
        return self.serialized_student_face_encodings

    def get_student_faces_image_urls(self):
        """
        Get the student faces image urls.
        """
        return self.student_faces_image_urls

    # setter methods

    def set_student_id(self, student_id):
        """
        Set the student id.
        """
        self.student_id = student_id

    def set_student_face_encodings(self, student_face_encodings):
        """
        Set the student face encodings.
        """
        self.student_face_encodings = student_face_encodings

    def set_number_of_faces(self, number_of_faces):
        """
        Set the number of faces.
        """
        self.number_of_faces = number_of_faces

    def set_serialized_student_face_encodings(self, serialized_student_face_encodings):
        """
        Set the serialized student face encodings.
        """
        self.serialized_student_face_encodings = serialized_student_face_encodings

    def set_student_faces_image_urls(self, student_faces_image_urls):
        """
        Set the student faces image urls.
        """
        self.student_faces_image_urls = student_faces_image_urls
