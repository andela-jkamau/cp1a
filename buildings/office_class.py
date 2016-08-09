from .room_class import Room


class Office(Room):
	
	"""
		This class extends the `Room` class by specifying it is an office and giving it a `people_allocated` property.
		people_allocated = A list of the identifiers of the people allocated to a room. 
	"""
	
	def __init__(self, room_capacity, room_name, room_type, people_allocated=[]):
		super().__init__(room_capacity, room_name, room_type)
		self.people_allocated = people_allocated
