from data import firebaseStorage
from io import BytesIO
import uuid
class AssistanceFirebase:
    def __init__(self):
        self.storage = firebaseStorage.fb_storage

    def upload_image(self, image):
        bucket = self.storage
        
        unique_name = str(uuid.uuid4())

        blob = bucket.blob(unique_name + ".jpg")

        image_stream = BytesIO(image)

        blob.upload_from_file(image_stream)

        blob.make_public()

        image_url = blob.public_url

        return image_url

    def upload_encoding(self, encoding):
        """
        encoding is a serialized pickle object
        """
        
        bucket = self.storage

        unique_name = str(uuid.uuid4())

        blob = bucket.blob(unique_name + ".pkl")

        encoding_stream = BytesIO(encoding)

        blob.upload_from_file(encoding_stream)

        blob.make_public()

        encoding_url = blob.public_url

        return encoding_url


    
