from pymongo import MongoClient
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["college_db"]
    attendance_collection = db["attendance"]
    print("MongoDB Connected Successfully!")
except Exception as e:
    print(f"Connection Failed: {e}")
