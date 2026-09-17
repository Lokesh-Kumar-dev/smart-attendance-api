from fastapi import FastAPI, BackgroundTasks
from database import attendance_collection
from models import Student
import time

app = FastAPI(title="Smart Attendance API - Lokesh Project")

# Difficult Task - Background Function
def send_email_task(roll_no: int):
    time.sleep(3)
    print(f"📧 Background Email sent to Roll No: {roll_no}")

@app.get("/")
def home():
    return {"message": "Welcome Lokesh, API is Running!"}

@app.post("/add-student")
def add_student(student: Student):
    # OOPS + MongoDB together
    attendance_collection.insert_one(student.dict())
    return {"status": "Success", "student": student.get_details()}

@app.get("/students")
def get_students():
    # JOIN logic here if you use SQL, for now MongoDB
    students = list(attendance_collection.find({}, {"_id": 0}))
    return {"total": len(students), "data": students}

@app.post("/mark-attendance/{roll_no}")
def mark_attendance(roll_no: int, background_tasks: BackgroundTasks):
    # Threading / Background Task - Most Difficult & Useful
    background_tasks.add_task(send_email_task, roll_no)
    return {"message": f"Attendance marked for {roll_no}"}

@app.delete("/delete-student/{roll_no}")
def delete_student(roll_no: int):
    attendance_collection.delete_one({"roll_no": roll_no})
    return {"message": f"Student {roll_no} deleted"}