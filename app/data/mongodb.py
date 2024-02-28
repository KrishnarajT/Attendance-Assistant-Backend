from pymongo import MongoClient
from config import mongodb_uri

def connect_to_mongo():
    client = MongoClient(mongodb_uri)
    db = client['Attendance']
    print("connected to mongo db!")
    return db

