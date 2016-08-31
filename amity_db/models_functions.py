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


def add_people(people_dict):
    """
    Takes a dictionary of people details and adds them to the database
    """

    try:
        for person in people_dict:
            person_db = PersonDetails(person_id=people_dict[person].identifier, name=people_dict[person].name, office=people_dict[person].office_allocated)
            try:
                person_db.living_space = people_dict[person].livingspace_allocated
                person_db.person_type = "Fellow"
            except AttributeError:
                person_db.person_type = "Staff"

            s.add(person_db)

        s.commit()
        s.close()
        return "People added to database successfully"
    except:
        return "Error in adding people to db"


def add_rooms(rooms_dict):
    """
    Takes a dictionary of room details and adds them to the database
    """

    for room in rooms_dict:
        pass
