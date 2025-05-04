"""
run facial recognition on an image file, by taking known_faces as input from other input known_faces files
"""

### importing libraries
import face_recognition

# Load image files using proper os path
import os

# Get the current file's directory
current_file_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_directory = os.path.dirname(current_file_directory)

# Get the directory of images
images_directory = os.path.join(parent_directory, "images")

# get the testing images directory
testing_images_directory = os.path.join(images_directory, "test")

image_files = []

# cycle through the known_faces directory and load each image

for filename in os.listdir(os.path.join(images_directory, "known_faces")):
    image_files.append(filename)

known_face_encodings = []

# Load the known images (create face encodings) for all image_files
for filename in image_files:
    image = face_recognition.load_image_file(
        os.path.join(images_directory, "known_faces", filename)
    )
    known_face_encodings.append(face_recognition.face_encodings(image)[0])

# Load all images in the test directory
test_image_files = []

for filename in os.listdir(testing_images_directory):
    test_image_files.append(filename)

unknown_face_encodings = {}

# create face encodings for all test images
for filename in test_image_files:
    image = face_recognition.load_image_file(
        os.path.join(testing_images_directory, filename)
    )
    unknown_face_encodings[filename] = face_recognition.face_encodings(image)


import face_recognition

# Load the known images (create face encodings)
image_of_person_1 = face_recognition.load_image_file("person_1.jpg")
person_1_face_encoding = face_recognition.face_encodings(image_of_person_1)[0]

image_of_person_2 = face_recognition.load_image_file("person_2.jpg")
person_2_face_encoding = face_recognition.face_encodings(image_of_person_2)[0]

# Create list of known face encodings
known_face_encodings = [person_1_face_encoding, person_2_face_encoding]

# Load the image we want to check
unknown_image = face_recognition.load_image_file("unknown.jpg")
unknown_face_encodings = face_recognition.face_encodings(unknown_image)

# There might be more than one person in the photo, so we need to check each face encoding
for unknown_face_encoding in unknown_face_encodings:
    # Test if this unknown face encoding matches any of the known face encodings
    results = face_recognition.compare_faces(
        known_face_encodings, unknown_face_encoding
    )

    name = "Unknown"

    if results[0]:
        name = "Person 1"
    elif results[1]:
        name = "Person 2"

    print(f"Found {name} in the photo!")
