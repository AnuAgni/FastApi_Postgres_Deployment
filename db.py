from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

url_db="postgresql://postgres:root@localhost:5432/form"

engine=create_engine(url_db)
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()