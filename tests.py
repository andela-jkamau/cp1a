import unittest

from buildings.amity_class import Amity
from buildings.livingspace_class import LivingSpace
from buildings.office_class import Office
from buildings.room_class import Room
from humans.fellow_class import Fellow
from humans.person_class import Person
from humans.staff_class import Staff


class TestClasses(unittest.TestCase):
	
	"""docstring for TestClassInitialization"""
	
	@classmethod
	def setUpClass(cls):
		cls._amity = Amity()
		cls._livingspace = LivingSpace()
		cls._office = Office()
		cls._room = Room()
		cls._fellow = Fellow()
		cls._person = Person()
		cls._staff = Staff()

	def test_class_initialization(self):
		self.assertIsInstance(self._amity, Amity, msg="Cannot create `Amity` instance")
		self.assertIsInstance(self._livingspace, LivingSpace, msg="Cannot create `LivingSpace` instance")
		self.assertIsInstance(self._office, Office, msg="Cannot create `Office` instance")