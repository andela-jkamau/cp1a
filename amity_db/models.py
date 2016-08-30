import os
import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base() 


class AmityRoom(Base):
    __tablename__ = 'amity_room'
    room_name = Column(String, unique=True, primary_key=True)
    room_capacity = Column(Integer)
    room_type = Column(String)


class PersonDetails(Base):
    __tablename__ = 'person_details'
    person_id = Column(Integer, primary_key=True)
    name = Column(String)
    person_type = Column(String)
    office = Column(String)
    living_space = Column(String)

db_name = 'test_amity_db.sqlite'

engine = create_engine('sqlite:///' + db_name)
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
