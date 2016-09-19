import os
import unittest
from unittest import mock
from io import StringIO
from contextlib import redirect_stdout
import humans.person_functions as person_functions
import buildings.room_functions as room_functions


class TestClasses(unittest.TestCase):
    """
        Tests for humans functionality
    """

    def setUp(self):
        self.person_args = {
            "<person_first_name>": "Jimmy",
            "<person_other_name>": "Kamau",
            "<person_type>": "Fellow",
            "<wants_accommodation>": "N"
        }
        person_functions.create_person(self.person_args)

    def test_create_person_with_no_rooms(self):

        # Test creation of person with empty office

        self.assertEqual(
            person_functions.people[1].name,
            "Jimmy Kamau",
            msg="Person being created with wrong name"
        )
        self.assertEqual(
            person_functions.people[1].office_allocated,
            None,
            msg="Person should have no office if none has been created"
        )
        self.assertFalse(
            person_functions.people[1].livingspace_allocated,
            msg="Person should have no living space if none has been created"
        )

    @mock.patch('builtins.input', side_effect=["L", "O"])
    def test_create_person_with_rooms(self, input):

        # Test creation of fellow with office and living space
        livingspace_args = {
            "<room_name>": ["Shell", "Go", "Ruby"]
        }
        office_args = {
            "<room_name>": ["Krypton", "Camelot", "Mordor"]
        }
        room_functions.create_room(livingspace_args)
        room_functions.create_room(office_args)

        person_args = {
            "<person_first_name>": "John",
            "<person_other_name>": "Doe",
            "<person_type>": "Fellow",
            "<wants_accommodation>": "Y"
        }
        person_functions.create_person(person_args)

        self.assertEqual(
            person_functions.people[2].name,
            "John Doe",
            msg="Person being created with wrong name"
        )
        self.assertNotEqual(
            person_functions.people[2].office_allocated,
            None,
            msg="Person not being allocated to an office"
        )
        self.assertNotEqual(
            person_functions.people[2].livingspace_allocated,
            None,
            msg="Person not being allocated to a living space"
        )

        # Test creation of fellow with office and no living space
        person_args["<person_first_name>"] = "Jane"
        person_args["<wants_accommodation>"] = "N"
        person_functions.create_person(person_args)

        self.assertEqual(
            person_functions.people[3].name,
            "Jane Doe",
            msg="Person being created with wrong name"
        )
        self.assertNotEqual(
            person_functions.people[3].office_allocated,
            None,
            msg="Person not being allocated to an office"
        )
        self.assertFalse(
            person_functions.people[3].livingspace_allocated,
            msg="Person being allocated to a living space"
            " when they don't want accommodation"
        )

        # Test creation of staff
        person_args["<person_first_name>"] = "Brian"
        person_args["<person_other_name>"] = "Ngure"
        person_args["<person_type>"] = "Staff"
        person_args["<wants_accommodation>"] = "Y"
        person_functions.create_person(person_args)

        self.assertNotEqual(
            person_functions.people[4].office_allocated,
            None,
            msg="Person not being allocated to an office"
        )
        self.assertRaises(
            AttributeError,
            lambda: person_functions.people[4].livingspace_allocated
        )

    @mock.patch('builtins.input', side_effect=["L", "O"])
    def test_load_people(self, input):
        """
            Test loading of people from a text file
        """
        livingspace_args = {
            "<room_name>": ["Shell", "Go", "Ruby"]
        }
        office_args = {
            "<room_name>": ["Krypton", "Camelot", "Mordor"]
        }
        room_functions.create_room(livingspace_args)
        room_functions.create_room(office_args)

        test_filename = "test_people.txt"
        people_to_load = "OLUWAFEMI SULE FELLOW Y\n"\
            "DOMINIC WALTERS STAFF\n"\
            "SIMON PATTERSON FELLOW Y\n"\
            "MARI LAWRENCE FELLOW Y\n"\
            "LEIGH RILEY STAFF\n"\
            "TANA LOPEZ FELLOW Y\n"\
            "KELLY McGUIRE STAFF N"

        if os.path.exists(test_filename):
            os.remove(test_filename)
        with open(test_filename, 'wt') as test_file:
            test_file.write(people_to_load)

        text_file_args = {
            "<filename>": test_filename
        }

        buf = StringIO()
        with redirect_stdout(buf):
            person_functions.load_people(text_file_args)
        self.assertGreater(
            len(person_functions.people),
            7,
            msg="People not being loaded from supplied text file"
        )

        os.remove(test_filename)

    @mock.patch('builtins.input', side_effect=["L", "O", "L", "O"])
    def test_reallocate_person(self, input):
        """
            Test people reallocation
        """

        livingspace_args = {
            "<room_name>": ["Bash"]
        }
        office_args = {
            "<room_name>": ["Valhalla"]
        }
        room_functions.create_room(livingspace_args)
        room_functions.create_room(office_args)

        person_args = {
            "<person_first_name>": "John",
            "<person_other_name>": "Doe",
            "<person_type>": "Fellow",
            "<wants_accommodation>": "Y"
        }
        person_functions.create_person(person_args)

        person_args["<person_first_name>"] = "Jane"
        person_args["<person_type>"] = "Staff"
        person_functions.create_person(person_args)

        livingspace_args["<room_name>"] = ["Ruby"]
        office_args["<room_name>"] = ["Krypton"]
        room_functions.create_room(livingspace_args)
        room_functions.create_room(office_args)

        # Test reallocation of person's office
        person_args = {
            "<person_identifier>": "3",
            "<new_room_name>": "Krypton"
        }
        person_functions.reallocate_person(person_args)

        self.assertEqual(
            person_functions.people[3].office_allocated,
            "Krypton",
            msg="Person not being reallocated to a new office"
        )
        self.assertIn(
            3,
            room_functions.current_rooms.rooms["Krypton"].people_allocated,
            msg="Person not being added to room's"
            " allocation list after reallocation"
        )
        self.assertNotIn(
            3,
            room_functions.current_rooms.rooms["Valhalla"].people_allocated,
            msg="Person not being removed from previous"
            " room after reallocation"
        )

        # Test reallocation of person's living space
        person_args["<person_identifier>"] = "2"
        person_args["<new_room_name>"] = "Ruby"
        person_functions.reallocate_person(person_args)

        self.assertEqual(
            person_functions.people[2].office_allocated,
            "Valhalla",
            msg="Person being reallocated to a new office"
            " instead of living space"
        )
        self.assertEqual(
            person_functions.people[2].livingspace_allocated,
            "Ruby",
            msg="Person not being reallocated to a new living space"
        )
        self.assertIn(
            2,
            room_functions.current_rooms.rooms["Ruby"].people_allocated,
            msg="Person not being added to room's"
            " allocation list after reallocation"
        )
        self.assertNotIn(
            2,
            room_functions.current_rooms.rooms["Bash"].people_allocated,
            msg="Person not being removed from previous"
            " room after reallocation"
        )

    def tearDown(self):
        room_functions.current_rooms.rooms = {}
        room_functions.current_rooms.available_offices = []
        room_functions.current_rooms.available_livingspaces = []
        person_functions.people = {}

    @classmethod
    def tearDownClass(self):
        room_functions.current_rooms.rooms = {}
        room_functions.current_rooms.available_offices = []
        room_functions.current_rooms.available_livingspaces = []
        person_functions.people = {}
        os.remove("test_amity_db.sqlite")
        os.remove("test_my_db.sqlite")


if __name__ == '__main__':
    unittest.main()
