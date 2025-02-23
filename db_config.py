from pymongo import MongoClient

MONGO_URI = "mongodb://192.168.1.8:27017/"
DATABASE_NAME = "mydatabase"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

users_collection = db["users"]
ats_collection = db["ats_score"]  
certificates_collection = db["certificates"]
