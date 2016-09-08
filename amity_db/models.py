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


class RoomOccupants(Base):
    __tablename__ = 'room_occupants'

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person_details.person_id'))
    room_id = Column(String, ForeignKey('amity_room.room_name'))

    person_details = relationship(PersonDetails)
    amity_room = relationship(AmityRoom)


class DbConnection(object):
    """
    Creates a db connection object
    """

    def __init__(self):
        self.db_name = 'test_amity_db.sqlite'
        self.engine = create_engine('sqlite:///' + self.db_name)
        self.session = sessionmaker()
        self.session.configure(bind=self.engine)
        Base.metadata.create_all(self.engine)
