import uuid


class Person(object):

	"""
		This class accepts `name` as its argument.
		name = Person's name 
	"""
	
	def __init__(self, name):
		self.name = name
		self.identifier = self.generate_unique_identifier() # Person's identifier

	def generate_unique_identifier(self):
		return uuid.uuid4()
