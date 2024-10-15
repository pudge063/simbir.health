from pydantic import BaseModel

class Timetable(BaseModel):
    timetable_id: int
    doctor_id: int
    hospital_id: str
    date: str
    time: str
    room: str
    

class Visit(BaseModel):
    visit_id: int
    timetable_id: int
    user_id: int

