import random


from .person_class import Person
from .fellow_class import Fellow
from .staff_class import Staff
import buildings.room_functions as room_functions


people = {}


def create_person(args):
    """
    Create person based on user's input
    """
    full_name = args["<person_first_name>"] + " " + args["<person_other_name>"]
    identifier = len(people) + 1
    person_details = [{
        "name": full_name,
        "identifier": identifier,
        "office_allocated": allocate_office(identifier)
    }]

    person_type = args["<person_type>"].upper()
    if person_type == "FELLOW":
        if args["<wants_accommodation>"] == "Y" or args["<wants_accommodation>"] == "y":
            person_details[0]["livingspace_allocated"] = allocate_livingspace(identifier)
        created_person = {person_details[0][
            "identifier"]: Fellow(**r) for r in person_details}

    elif person_type == "STAFF":
        created_person = {person_details[0][
            "identifier"]: Staff(**r) for r in person_details}

    else:
        return "Allowed person type is either Fellow or Staff"

    try:
        people.update(created_person)
        message = "{} {} has been added to the system. The office: {}".format(
            person_type,
            created_person[identifier].name,
            created_person[identifier].office_allocated)
        if person_type == "FELLOW":
            if created_person[identifier].livingspace_allocated:
                message += ", and living space: {}".format(
                    created_person[identifier].livingspace_allocated)
        message += " has been allocated to them"

    except:
        message = "Error encountered while adding the person to the system"

    return message


def allocate_office(identifier):
    if len(room_functions.current_rooms.available_offices) > 0:
        office = str(random.choice(room_functions.current_rooms.available_offices))
        allocated_office = room_functions.current_rooms.rooms[office]
        allocated_office.add_person_to_room(identifier)
        return allocated_office.room_name
    else:
        return None


def allocate_livingspace(identifier):
    if len(room_functions.current_rooms.available_livingspaces) > 0:
        living = str(random.choice(room_functions.current_rooms.available_livingspaces))
        allocated_living = room_functions.current_rooms.rooms[living]
        allocated_living.add_person_to_room(identifier)
        return allocated_living.room_name
    else:
        return None


def reallocate_person(args):
    """
    Reallocate a person from one room to another 
    """

    person_id = int(args["person_identifier"])
    if person_id in list(people.keys()):
        person = people[person_id]
        new_room = args["new_room_name"]
        rooms_at_amity = room_functions.current_rooms
        if new_room not in rooms_at_amity.available_livingspaces and new_room not in rooms_at_amity.available_offices:
            return "The new room either doesn't exist or is full"
        else:
            pass
    else:
        return "There is no person with the given identifier"
