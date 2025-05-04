from dotenv import load_dotenv
import os

load_dotenv()

mongodb_uri = os.getenv("MONGODB_URI")
apiKey = os.getenv("apiKey")
authDomain = os.getenv("authDomain")
projectId = os.getenv("projectId")
storageBucket = os.getenv("storageBucket")
messagingSenderId = os.getenv("messagingSenderId")
appId = os.getenv("appId")
measurementId = os.getenv("measurementId")

port = os.getenv("PORT")
