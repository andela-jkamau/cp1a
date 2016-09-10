import unittest
from unittest import mock
import buildings.room_functions as room_functions
import humans.person_functions as person_functions


class TestClasses(unittest.TestCase):

    """
            Tests for program's continuous development.
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
        self.assertTrue(
            "Valhalla" in
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
        self.assertTrue(
            "Bash" in
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
        person_args = {
            "<person_first_name>": "Jane",
            "<person_other_name>": "Doe",
            "<person_type>": "Fellow",
            "<wants_accommodation>": "N"
        }
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
        person_args = {
            "<person_first_name>": "Brian",
            "<person_other_name>": "Ngure",
            "<person_type>": "Staff",
            "<wants_accommodation>": False
        }
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


if __name__ == '__main__':
    unittest.main()
