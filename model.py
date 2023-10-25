from sqlalchemy import Column,String,Integer,Date
from db import Base

class Form(Base):
    __tablename__ = 'Basic_info'
    name=Column(String)
    age=Column(Integer)
    dob=Column(Date,primary_key=True)

