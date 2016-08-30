from sqlalchemy import *
from .models import Base, AmityRoom, PersonDetails, session, engine


Base.metadata.bind = engine
s = session()


def populate_people():
    """
    Returns a dictionary with details about all people saved to the database
    """

    people = s.query(PersonDetails).all()
    return people 
