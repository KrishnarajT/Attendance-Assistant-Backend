# Main Class file for FaceRecognition
# import face_recognition
import threading
import pickle
import requests
import io
from PIL import Image
import numpy as np
import face_recognition
import cv2
from services.student_services import get_student_from_id
from services.assistanceFirebase import AssistanceFirebase


# import services


class FaceRec:
    """
    Contains methods for facial recognition of multiple students, being present in a single image. So basically if you
    wanna get the attendance of a class, you have to instantiate this class, and then call the methods to get the
    attendance. It contains all the methods that will actually perform the facial recognition using multithreading.
    After you are done you can simply delete the object, and all the data will be cleaned up.
    """

    def __init__(
        self,
        student_face_encodings: dict,
        class_images: list,
        panel_id: str,
        student_ids: list,
        room_id: str,
    ):
        """
        :param student_face_encodings: dictionary containing the face encodings of the students. The keys are the
        student ids, and the values are the face encodings of the students.
        :param class_images: list of images of the class. from pi or from the client app.
        :param panel_id: the id of the panel.
        :param student_ids: list of student ids.

        """
        if student_face_encodings is None:
            student_face_encodings = {}
        print("Init Face Recognition!")
        self.student_face_encodings = student_face_encodings
        self.class_images = class_images
        self.room_id = room_id
        self.panel_id = panel_id
        self.students_present = []
        self.students_absent = []
        self.student_ids = student_ids
        self.last_class_image_url = None

    def get_last_scanned_class_image(self):
        return self.last_class_image_url

    def get_image_from_url(self, image_url):
        print("now doing", image_url)
        response = requests.get(image_url)
        image_bytes = io.BytesIO(response.content)

        # Open the image with PIL so we can use it with face_recognition
        image = Image.open(image_bytes)

        # Convert the image to a numpy array so face_recognition can work with it
        image_np = np.array(image)
        return image_np

    def get_encodings_from_url(self, encoding_url):
        response = requests.get(encoding_url)
        response.raise_for_status()  # Ensure we got a valid response

        # Use BytesIO to handle the byte stream
        bytes_io = io.BytesIO(response.content)

        # convert back from pickle to the face encodings
        face_encodings = pickle.load(bytes_io)
        # print(face_encodings)
        return face_encodings

    def process_face_encodings(self):
        """
        Process the face encodings of the students.
        # student face encodings is a dictionary with student id as key and face encodings url as value.
        The url is of a pickle file. we have to load the pickle file and get the face encodings.
        """
        # load the face encodings
        for student_id in self.student_face_encodings:
            # get the face encodings
            face_encodings = self.get_encodings_from_url(
                self.student_face_encodings[student_id]
            )

            # replace the url with the face encodings
            self.student_face_encodings[student_id] = face_encodings

    def find_attendance(self):
        """
        Perform the facial recognition on the class images, and return the attendance.
        """

        # check if the student face encodings are a string or a face encoding object.
        if isinstance(list(self.student_face_encodings.values())[0], str):
            self.process_face_encodings()
        else:
            print("Face encodings are already loaded!")

        # create threads for each image
        threads = []
        for image in self.class_images:
            print("creating tread for image", image)
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
        image = self.get_image_from_url(image)
        # get the face locations
        face_locations = face_recognition.face_locations(image)
        image_cp = image.copy()
        # save the face locations by drawing a rectangle around the face
        for top, right, bottom, left in face_locations:
            # draw a rectangle around the face
            cv2.rectangle(image_cp, (left, top), (right, bottom), (0, 0, 255), 2)

        # save the iamge
        cv2.imwrite("face_locations_for_class.jpg", image_cp)
        fb_storage = AssistanceFirebase()

        with open("face_locations_for_class.jpg", "rb") as f:
            image_cp = f.read()
            fb_storage.upload_image(image_cp)
            self.last_class_image_url = fb_storage.get_image_url()

        # get the face encodings
        face_encodings = face_recognition.face_encodings(
            image, face_locations, num_jitters=10
        )

        # check if the face encodings match with the students' face encodings
        for _, face_encoding in enumerate(face_encodings):
            print("trying for encoding no. ", _)
            # compare the face encodings for each element of the array for each student
            for student_id in self.student_face_encodings:
                student = get_student_from_id(student_id)
                print("now testing for student:")
                print(student["name"])
                # print(self.student_face_encodings[student_id])
                print(len(self.student_face_encodings[student_id]))
                # compare the face encodings
                matches = face_recognition.compare_faces(
                    self.student_face_encodings[student_id], face_encoding
                )
                print("matches", matches)
                # if the face encodings match
                if True in matches:
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
