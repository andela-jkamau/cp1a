from .amity_class import Amity
from .room_class import Room
from .office_class import Office
from .livingspace_class import LivingSpace


current_rooms = Amity()

def create_room(args):
	"""
	Create rooms based on user's input
	"""

	if not args["OFFICE"] and not args["LIVINGSPACE"]:
		message = "Please specify if the room is an office or living space"

	elif args["OFFICE"]:
		rooms = [{"room_capacity": 6, "room_name": r, "room_type": "office"} for r in args["<room_name>"]]
		created_rooms = {r["room_name"]: Office(**r) for r in rooms}

	elif args["LIVINGSPACE"]:
		rooms = [{"room_capacity": 4, "room_name": r, "room_type": "living space"} for r in args["<room_name>"]]
		created_rooms = {r["room_name"]: LivingSpace(**r) for r in rooms}

	try:
		current_rooms.rooms.update(created_rooms)
		message = "The rooms"
		for room in args["<room_name>"]:
			message += " " + str(room)
		message += " have been created successfully"

	except:
		message = "Error encountered while creating rooms"

	return(message)

def list_rooms():
	"""
	List the rooms in Amity. Returns a dictionary of the rooms
	"""

	return current_rooms.rooms
