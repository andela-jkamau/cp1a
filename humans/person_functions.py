import random
import sys
from .fellow_class import Fellow
from .staff_class import Staff
import buildings.room_functions as room_functions
from amity_db.models_functions import \
    populate_people, add_people, remove_person_from_room_db


people = {}


def populate_people_from_db():
    people_from_db = populate_people()
    for person in people_from_db:
        person_details = [{
            "name": person.name,
            "identifier": person.person_id,
            "office_allocated": person.office
        }]
        if person.person_type == "Fellow":
            person_details[0]["livingspace_allocated"] = person.living_space
            created_person = {
                person_details[0]["identifier"]: Fellow(**r)
                for r in person_details
            }
        elif person.person_type == "Staff":
            created_person = {
                person_details[0]["identifier"]: Staff(**r)
                for r in person_details}
        people.update(created_person)
    return " [*] People successfully loaded from database...\n"


def create_person(args):
    """
    Create person based on user's input
    """

    full_name = args["<person_first_name>"] + " " + args["<person_other_name>"]
    for person in people:
        if people[person].name == full_name:
            return "{} already exists".format(people[person].name)

    identifier = len(people) + 1
    person_details = [{
        "name": full_name,
        "identifier": identifier,
        "office_allocated": allocate_office(identifier)
    }]

    person_type = args["<person_type>"].upper()
    if person_type == "FELLOW":
        if args["<wants_accommodation>"] == "Y" or \
                args["<wants_accommodation>"] == "y":
            person_details[0]["livingspace_allocated"] = \
                allocate_livingspace(identifier)
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

    except Exception:
        message = "Error encountered while adding the person to the system"

    return message


def allocate_office(identifier):
    if len(room_functions.current_rooms.available_offices) > 0:
        office = str(
            random.choice(room_functions.current_rooms.available_offices)
        )
        allocated_office = room_functions.current_rooms.rooms[office]
        allocated_office.add_person_to_room(identifier)
        return allocated_office.room_name
    else:
        return None


def allocate_livingspace(identifier):
    if len(room_functions.current_rooms.available_livingspaces) > 0:
        living = str(random.choice(
            room_functions.current_rooms.available_livingspaces))
        allocated_living = room_functions.current_rooms.rooms[living]
        allocated_living.add_person_to_room(identifier)
        return allocated_living.room_name
    else:
        return None


def reallocate_person(args):
    """
    Reallocate a person from one room to another
    """

    person_id = int(args["<person_identifier>"])
    if person_id in list(people.keys()):
        new_room = args["<new_room_name>"]
        rooms_at_amity = room_functions.current_rooms
        if new_room not in rooms_at_amity.available_livingspaces and \
                new_room not in rooms_at_amity.available_offices:
            return "The new room either doesn't exist or is full"
        else:
            if new_room in rooms_at_amity.available_offices:
                current_person_room = people[person_id].office_allocated
                people[person_id].office_allocated = new_room
            elif new_room in rooms_at_amity.available_livingspaces:
                current_person_room = people[person_id].livingspace_allocated
                people[person_id].livingspace_allocated = new_room
            rooms_at_amity.\
                rooms[current_person_room].\
                remove_person_from_room(person_id)
            remove_person_from_room_db(person_id, current_person_room)
            rooms_at_amity.rooms[new_room].add_person_to_room(person_id)
            return "{} has been moved to {}".\
                format(people[person_id].name, new_room)
    else:
        return "There is no person with the given identifier"


def get_person_name(person_id):
    """
    Return person's name given their ID
    """

    try:
        return people[person_id].name
    except Exception:
        return False


def load_people(args):
    """
    Adds people to rooms from a txt file
    """

    filename = args["<filename>"]
    try:
        with open(filename, 'r') as f:
            file_read = f.readlines()
        for person in file_read:
            person = person.split()
            my_args = {
                '<person_first_name>': person[0],
                '<person_other_name>': person[1],
                '<person_type>': person[2],
                '<wants_accommodation>': person[3]
                if len(person) > 3 else None}
            print (create_person(my_args))
        message = "Finished adding people"
    except Exception:
        message = "Error while adding people to system"

    return message


def print_unallocated(args):
    """
    Returns unallocated people
    """
    message = ""

    for person in people:
        if people[person].office_allocated is None:
            message += "{} hasn't been allocated to an office".\
                format(people[person].name)
            try:
                persons_name = people[person].name
                message += " or a living space".\
                    format(persons_name) if \
                    people[person].livingspace_allocated is None else ""
            except AttributeError:
                message += ""
            message += "\n"

        else:
            try:
                message += "{} hasn't been allocated to a living space\n".\
                    format(people[person].name) if \
                    people[person].livingspace_allocated is None else ""
            except AttributeError:
                message += ""

    if args['-o'] and ['<file_location>'] is not None:
        filename = args['<file_location>']
        try:
            with open(filename, 'wt') as f:
                f.write(message)
            message = "Unallocations have been printed to {}".format(filename)
        except Exception:
            message = str(sys.exc_info()[0])
    elif (
        args['<file_location>'] is not None and
        args['-o'] is False
    ) or (
        args['-o'] is not False and
        args['<file_location>'] is None
    ):
        message = "Specify the file to output to after the `-o` argument"

    return message


def get_person_id(args):
    """
    Returns a person's ID when given their name.
    Useful when reallocating people
    """

    person_name = "{} {}".\
        format(args["<person_first_name>"], args["<person_other_name>"])

    for person in people:
        if people[person].name == person_name:
            return "{} has ID Number {}".\
                format(person_name, people[person].identifier)

    return "The person with the name given doesn't exist in the system"


def add_people_to_db():
    return add_people(people)
