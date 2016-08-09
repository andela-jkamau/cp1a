from .room_class import Room


class LivingSpace(Room):

	"""
		This class extends the `Room` class by specifying it is a living space and giving it a `people_allocated` property.
		people_allocated = A list of the identifiers of the people allocated to a room. 
	"""
	
	def __init__(self, people_allocated=[], **kwargs):
		super().__init__(**kwargs)
		self.people_allocated = people_allocated

	def add_person_to_room(self, person_name):
		if len(self.people_allocated) < self.room_capacity:
			self.people_allocated.append(person_name)
		else:
			return "ROOM FULL"
