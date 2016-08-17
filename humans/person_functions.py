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
	person_details = [{"name":full_name, "identifier":identifier, "office_allocated":allocate_office(identifier), "livingspace_allocated":allocate_livingspace(identifier)}]
	
	if args["FELLOW"]:
		created_person = {person_details[0]["identifier"]: Fellow(**r) for r in person_details}
		person_type = "Fellow"

	elif args["STAFF"]:
		created_person = {person_details[0]["identifier"]: Staff(**r) for r in person_details}
		person_type = "Staff"

	try:
		people.update(created_person)
		message = "{} {} has been added to the system. The office: {}".format(person_type, created_person[identifier].name, created_person[identifier].office_allocated)
		if created_person[identifier].livingspace_allocated:
			message += ", and living space {}".format(created_person[identifier].livingspace_allocated)
		message += " has been allocated to them"

	except:
		message = "Error encountered while adding the person to the system"
	
	return message


def allocate_office(identifier):
	room = next(iter(room_functions.current_rooms.rooms))
	return room


def allocate_livingspace(identifier):
	return False
