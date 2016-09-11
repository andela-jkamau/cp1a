import os
import unittest
from unittest import mock
from io import StringIO
from contextlib import redirect_stdout
import buildings.room_functions as room_functions
import humans.person_functions as person_functions


class TestClasses(unittest.TestCase):

    """
        Tests for program's continuous development.
        Tests are named `test_n` for them to be run
            in a sequential manner
    """

    def test_1_person_creation_with_no_rooms(self):

        # Test creation of person with empty office
        person_args = {
            "<person_first_name>": "Jimmy",
            "<person_other_name>": "Kamau",
            "<person_type>": "Fellow",
            "<wants_accommodation>": "N"
        }
        person_functions.create_person(person_args)

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

    @mock.patch('builtins.input', side_effect=["O"])
    def test_2_office_creation(self, input):

        # Test creation of office
        office_args = {
            "<room_name>": ["Valhalla"]
        }
        room_functions.create_room(office_args)

        self.assertEqual(
            len(room_functions.current_rooms.rooms),
            1,
            msg="Cannot create a new room"
        )
        self.assertIn(
            "Valhalla",
            room_functions.current_rooms.available_offices,
            msg="Empty room not being added to list of available rooms"
        )

    @mock.patch('builtins.input', side_effect=["L"])
    def test_3_living_space_creation(self, input):

        # Test creation of living space
        living_space_args = {
            "<room_name>": ["Bash"]
        }
        room_functions.create_room(living_space_args)

        self.assertEqual(
            len(room_functions.current_rooms.rooms),
            2,
            msg="Cannot create more than one room"
        )
        self.assertIn(
            "Bash",
            room_functions.current_rooms.available_livingspaces,
            msg="Empty living space not being added to list of available living spaces"
        )

    def test_4_person_creation_with_rooms(self):

        # Test creation of fellow with office and living space
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
        self.assertEqual(
            person_functions.people[2].office_allocated,
            "Valhalla",
            msg="Person not being allocated to an office"
        )
        self.assertEqual(
            person_functions.people[2].livingspace_allocated,
            "Bash",
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
        self.assertEqual(
            person_functions.people[3].office_allocated,
            "Valhalla",
            msg="Person not being allocated to an office"
        )
        self.assertFalse(
            person_functions.people[3].livingspace_allocated,
            msg="Person being allocated to a living space when they don't want accommodation"
        )

        # Test creation of staff
        person_args["<person_first_name>"] = "Brian"
        person_args["<person_other_name>"] = "Ngure"
        person_args["<person_type>"] = "Staff"
        person_args["<wants_accommodation>"] = False
        person_functions.create_person(person_args)

        self.assertEqual(
            person_functions.people[4].office_allocated,
            "Valhalla",
            msg="Person not being allocated to an office"
        )
        self.assertRaises(
            AttributeError,
            lambda: person_functions.people[4].livingspace_allocated,
        )

    @mock.patch('builtins.input', side_effect=["O"])
    def test_5_multiple_office_creation(self, input):

        # Test creation of office
        office_args = {
            "<room_name>": ["Krypton", "Camelot", "Mordor"]
        }
        room_functions.create_room(office_args)

        self.assertEqual(
            len(room_functions.current_rooms.rooms),
            5,
            msg="Cannot create multiple rooms"
        )
        self.assertIn(
            "Camelot",
            room_functions.current_rooms.available_offices,
            msg="Empty rooms not being added to list of available rooms"
        )

    @mock.patch('builtins.input', side_effect=["L"])
    def test_6_multiple_living_space_creation(self, input):

        # Test creation of office
        office_args = {
            "<room_name>": ["Shell", "Go", "Ruby"]
        }
        room_functions.create_room(office_args)

        self.assertEqual(
            len(room_functions.current_rooms.rooms),
            8,
            msg="Cannot create multiple rooms"
        )
        self.assertIn(
            "Go",
            room_functions.current_rooms.available_livingspaces,
            msg="Empty rooms not being added to list of available rooms"
        )

    def test_7_load_people(self):
        """
            Test loading of people from a text file
        """

        text_file_args = {
            "<filename>": "test_people.txt"
        }
        buf = StringIO()
        with redirect_stdout(buf):
            person_functions.load_people(text_file_args)

        self.assertGreater(
            len(person_functions.people),
            7,
            msg="People not being loaded from supplied text file"
        )

    def test_8_reallocate_person(self):
        """
            Test people reallocation
        """

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
            msg="Person not being added to room's allocation list after reallocation"
        )
        self.assertNotIn(
            3,
            room_functions.current_rooms.rooms["Valhalla"].people_allocated,
            msg="Person not being removed from previous room after reallocation"
        )

        # Test reallocation of person's living space
        person_args["<person_identifier>"] = "2"
        person_args["<new_room_name>"] = "Ruby"
        person_functions.reallocate_person(person_args)

        self.assertEqual(
            person_functions.people[2].office_allocated,
            "Valhalla",
            msg="Person being reallocated to a new office instead of living space"
        )
        self.assertEqual(
            person_functions.people[2].livingspace_allocated,
            "Ruby",
            msg="Person not being reallocated to a new living space"
        )
        self.assertIn(
            2,
            room_functions.current_rooms.rooms["Ruby"].people_allocated,
            msg="Person not being added to room's allocation list after reallocation"
        )
        self.assertNotIn(
            2,
            room_functions.current_rooms.rooms["Bash"].people_allocated,
            msg="Person not being removed from previous room after reallocation"
        )

    def test_9_print_allocations(self):
        """
            Test printing of allocations
        """

        allocations_args = {
            "-o": False,
            "<file_location>": None
        }

        # Test printing of allocations to screen
        """buf = StringIO()
        with redirect_stdout(buf):
            room_functions.print_allocations(allocations_args)
        self.assertTrue(
            any(
                "TANA LOPEZ," in text
                for text in [buf.getvalue()]
            )
        )"""

        # Test printing of allocations to file
        output_file = "test_print_unallocations.txt"
        if os.path.exists(output_file):
            os.remove(output_file)
        allocations_args["-o"] = True
        allocations_args["<file_location>"] = output_file
        room_functions.print_allocations(allocations_args)

        with open(output_file, 'r') as read_output:
            self.assertTrue(
                any(
                    "SIMON PATTERSON," in text
                    for text in read_output.readlines()
                )
            )
        os.remove(output_file)


if __name__ == '__main__':
    unittest.main()
