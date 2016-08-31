from sqlalchemy import *
from .models import Base, AmityRoom, PersonDetails, RoomOccupants, session, engine


Base.metadata.bind = engine
s = session()


def populate_people():
    """
    Returns a dictionary with details about all people saved to the database
    """

    people = s.query(PersonDetails).all()
    return people


def populate_rooms():
    """
    Returns a dictionary with details about the rooms saved to the database
    """

    rooms = s.query(AmityRoom).all()
    return rooms


def populate_room_occupants(room_name):
    """
    Returns the occupants of `room_name` from the database
    """

    occupants = s.query(RoomOccupants).filter_by(room_id=room_name).all()
    return occupants


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
        room_db = AmityRoom(room_name=rooms_dict[room].room_name, room_capacity=rooms_dict[room].room_capacity, room_type=rooms_dict[room].room_type)
        s.add(room_db)
        
        for person in rooms_dict[room].people_allocated:
            occupant = RoomOccupants(person_id=person, room_id=room_db.room_name)
            s.add(occupant)

        s.commit()
    
    s.close()
    return "Rooms added to database successfully"
