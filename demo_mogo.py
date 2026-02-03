from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://127.0.0.1:27017")
db = client["secure_db"]
users = db["users"]

# WRITE
result = users.insert_one({
    "name": "Nagsrujan",
    "email": "nags@example.com",
    "created_at": datetime.utcnow()
})
print("Inserted ID:", result.inserted_id)

# READ
user = users.find_one({"email": "nags@example.com"}, {"_id": 0})
print("User:", user)

