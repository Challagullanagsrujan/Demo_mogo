from pymongo import MongoClient
import datetime

# Connect to local MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['encrypted_test_db']
collection = db['test_collection']

# Insert a test record
test_record = {
    "author": "CloudServer",
    "text": "This data is stored on LUKS!",
    "date": datetime.datetime.now()
}

print("Inserting data...")
rec_id = collection.insert_one(test_record).inserted_id
print(f"Data inserted with ID: {rec_id}")

# Find and print it back
print("Reading data back...")
print(collection.find_one({"_id": rec_id}))