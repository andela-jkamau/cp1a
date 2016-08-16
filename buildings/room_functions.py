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
		print("Please specify if the room is an office or living space")

	elif args["OFFICE"]:
		rooms = [{"room_capacity": 6, "room_name": r, "room_type": "office"} for r in args["<room_name>"]]
		created_rooms = {r["room_name"]: Office(**r) for r in rooms}

	elif args["LIVINGSPACE"]:
		rooms = [{"room_capacity": 4, "room_name": r, "room_type": "living space"} for r in args["<room_name>"]]
		created_rooms = {r["room_name"]: LivingSpace(**r) for r in rooms}

	try:
		current_rooms.rooms.update(created_rooms)
		print("The rooms" \
		+ str(args["<room_name>"]) \
		+ "have been created successfully")

	except:
		print("Error encountered while creating rooms")
