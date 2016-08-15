import unittest
from subprocess import getoutput

from buildings.amity_class import Amity
from buildings.livingspace_class import LivingSpace
from buildings.office_class import Office
from buildings.room_class import Room
from humans.fellow_class import Fellow
from humans.person_class import Person
from humans.staff_class import Staff


class TestClasses(unittest.TestCase):
	
	"""
		Tests for program's continuous development.
	"""
	
	@classmethod
	def setUpClass(cls):
		cls._amity = Amity()
		cls._livingspace = LivingSpace(room_capacity=4, room_name="Bash", room_type="living space")
		cls._office = Office(room_capacity=4, room_name="Hogwarts", room_type="office")
		cls._room = Room(4, "Oculus", "office")
		cls._fellow = Fellow(name="John Doe")
		cls._person = Person("John Doe")
		cls._staff = Staff(name="John Doe")

	def test_class_initialization(self):
		self.assertIsInstance(
			self._amity, Amity,
			msg="Cannot create `Amity` instance")
		self.assertIsInstance(
			self._livingspace, LivingSpace,
			msg="Cannot create `LivingSpace` instance")
		self.assertIsInstance(
			self._office, Office,
			msg="Cannot create `Office` instance")
		self.assertIsInstance(
			self._room, Room,
			msg="Cannot create `Room` instance")
		self.assertIsInstance(
			self._fellow, Fellow,
			msg="Cannot create `Fellow` instance")
		self.assertIsInstance(
			self._person, Person,
			msg="Cannot create `Person` instance")
		self.assertIsInstance(
			self._staff, Staff,
			msg="Cannot create `Staff` instance")

	def test_commands_callability(self):
		self.assertEqual(getoutput(["./amity.py -h"]), 'Welcome to Amity. Amity helps you allocate rooms to people at random.\nUsage:\n    amity create_room <room_name>...\n    amity add_person <person_name> <FELLOW|STAFF> [wants_accommodation]\n    amity reallocate_person <person_identifier> <new_room_name>\n    amity load_people [-f=filename]\n    amity print_allocations [-o=filename]\n    amity print_unallocated [-o=filename]\n    amity print_room <room_name>\n    amity save_state [--db=sqlite_database]\n    amity load_state <sqlite_database>\n    amity (-i | --interactive)\n    amity (-h | --help)\nOptions:\n    -i, --interactive  Interactive Mode\n    -h, --help  Show this screen and exit.')



if __name__ == '__main__':
	unittest.main()
