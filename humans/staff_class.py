from .person_class import Person


class Staff(Person):

	"""
		This is a sub-class of the `Person` class. It holds information about a Staff.
		The class extends the `Person` class by giving it an `office_allocated` property.
		`office_allocated` defaults to False.
		office_allocated = The ID of the office the Fellow has been allocated to.
	"""
	
	def __init__(self, office_allocated=False, **kwargs):
		super().__init__(**kwargs)
		self.office_allocated = office_allocated
