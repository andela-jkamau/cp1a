import os
import unittest
from unittest import mock
import buildings.room_functions as room_functions
import humans.person_functions as person_functions


class TestClasses(unittest.TestCase):
    """
        Tests for buildings functionality
    """

    @mock.patch('builtins.input', side_effect=["O"])
    def test_office_creation(self, input):

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
    def test_living_space_creation(self, input):

        # Test creation of living space
        living_space_args = {
            "<room_name>": ["Bash"]
        }
        room_functions.create_room(living_space_args)

        self.assertIn(
            "Bash",
            room_functions.current_rooms.available_livingspaces,
            msg="Empty living space not being added"
            " to list of available living spaces"
        )

    @mock.patch('builtins.input', side_effect=["O"])
    def test_multiple_office_creation(self, input):

        # Test creation of office
        office_args = {
            "<room_name>": ["Krypton", "Camelot", "Mordor"]
        }
        room_functions.create_room(office_args)

        self.assertEqual(
            len(room_functions.current_rooms.rooms),
            3,
            msg="Cannot create multiple rooms"
        )
        self.assertIn(
            "Camelot",
            room_functions.current_rooms.available_offices,
            msg="Empty rooms not being added to list of available rooms"
        )

    @mock.patch('builtins.input', side_effect=["L"])
    def test_multiple_living_space_creation(self, input):

        # Test creation of office
        livingspace_args = {
            "<room_name>": ["Shell", "Go", "Ruby"]
        }
        room_functions.create_room(livingspace_args)

        self.assertEqual(
            len(room_functions.current_rooms.rooms),
            3,
            msg="Cannot create multiple rooms"
        )
        self.assertIn(
            "Go",
            room_functions.current_rooms.available_livingspaces,
            msg="Empty rooms not being added to list of available rooms"
        )

    @mock.patch('builtins.input', side_effect=["L", "O"])
    def test_print_allocations(self, input):
        """
            Test printing of allocations
        """

        livingspace_args = {
            "<room_name>": ["Shell", "Go", "Ruby"]
        }
        office_args = {
            "<room_name>": ["Krypton", "Camelot", "Mordor"]
        }
        room_functions.create_room(livingspace_args)
        room_functions.create_room(office_args)

        person_args = {
            "<person_first_name>": "TANA",
            "<person_other_name>": "LOPEZ",
            "<person_type>": "Fellow",
            "<wants_accommodation>": "Y"
        }
        person_functions.create_person(person_args)
        person_args = {
            "<person_first_name>": "SIMON",
            "<person_other_name>": "PATTERSON",
            "<person_type>": "Staff",
            "<wants_accommodation>": None
        }
        person_functions.create_person(person_args)

        allocations_args = {
            "-o": False,
            "<file_location>": None
        }

        # Test printing of allocations to screen
        allocations = room_functions.print_allocations(allocations_args)
        self.assertTrue(
            any(
                "TANA LOPEZ," in text
                for text in [allocations]
            )
        )

        # Test printing of allocations to file
        output_file = "test_print_allocations.txt"
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
        person_functions.people = {}

    def test_print_unallocated(self):
        """
            Test printing of unallocated
        """
        person_args = {
            "<person_first_name>": "Jimmy",
            "<person_other_name>": "Kamau",
            "<person_type>": "Fellow",
            "<wants_accommodation>": "Y"
        }
        person_functions.create_person(person_args)

        unallocated_args = {
            "-o": False,
            "<file_location>": None
        }

        # Test printing of unallocated to screen
        unallocated = person_functions.print_unallocated(unallocated_args)
        self.assertTrue(
            any(
                "Jimmy Kamau" in text
                for text in [unallocated]
            )
        )

        # Test printing of unallocated to file
        output_file = "test_print_unallocated.txt"
        if os.path.exists(output_file):
            os.remove(output_file)

        unallocated_args["-o"] = True
        unallocated_args["<file_location>"] = output_file
        person_functions.print_unallocated(unallocated_args)

        with open(output_file, 'r') as read_output:
            self.assertTrue(
                any(
                    "Jimmy Kamau" in text
                    for text in read_output.readlines()
                )
            )

        os.remove(output_file)
        person_functions.people = {}

    def tearDown(self):
        room_functions.current_rooms.rooms = {}
        room_functions.current_rooms.available_livingspaces = []
        room_functions.current_rooms.available_offices = []


if __name__ == '__main__':
    unittest.main()
