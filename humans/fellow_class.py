from .person_class import Person


class Fellow(Person):
	
	"""
		This is a sub-class of the `Person` class. It holds information about a Fellow.
		The class extends the `Person` class by giving it `office_allocated` and `livingspace_allocated` properties.
		`office_allocated` and `livingspace_allocated` default to False.
		office_allocated = The ID of the office the Fellow has been allocated to.
		livingspace_allocated = The ID of the living space the Fellow has been allocated to.
	"""
	
	def __init__(self, office_allocated=False, livingspace_allocated=False):
		self.office_allocated = office_allocated
		self.livingspace_allocated = livingspace_allocated
		