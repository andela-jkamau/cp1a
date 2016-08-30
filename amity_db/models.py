import os
import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base() 


class AmityRoom(Base):
    __table__ = 'amity_room'
    room_name = Column(String, unique=True)
    room_capacity = Column(Integer)
    room_type = Column(String)


class PersonDetails(Base):
    __table__ = 'person_details'
    person_id = Column(Integer, primary_key=True)
    name = Column(String)
    person_type = Column(String)
    office = Column(String)
    living_space = Column(String)
