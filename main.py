from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
from datetime import date
from db import engine, SessionLocal
from sqlalchemy.orm import Session
import model

app=FastAPI()

model.Base.metadata.create_all(bind=engine)

class FormBase(BaseModel):
    name: str
    age: int
    dob: date=None

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/persons")
async def create_person(person: FormBase,db:Session=Depends(get_db)):
    db_person=model.Form(name=person.name,age=person.age,dob=person.dob)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)

