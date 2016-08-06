from .room_class import Room


class LivingSpace(Room):

	"""
		This class extends the `Room` class by specifying it is a living space and giving it a `people_allocated` property.
		people_allocated = A list of the identifiers of the people allocated to a room. 
	"""
	
	def __init__(self, people_allocated):
		self.people_allocated = people_allocated
