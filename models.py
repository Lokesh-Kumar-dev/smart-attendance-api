from pydantic import BaseModel

# OOPS - This is used everywhere
class Student(BaseModel):
    roll_no: int
    name: str
    branch: str
    city: str = "Machilipatnam"

    # OOPS Method
    def get_details(self):
        return f"{self.roll_no} - {self.name} from {self.branch}"