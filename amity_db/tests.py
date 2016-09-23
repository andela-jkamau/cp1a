import os
import unittest
from unittest import mock
import humans.person_functions as person_functions
import buildings.room_functions as room_functions
import amity_db.models_functions as amity_models


class TestClasses(unittest.TestCase):
    """
        Tests for database functionality
    """

    @mock.patch('builtins.input', side_effect=["L", "O"])
    def setUp(self, input):
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

        person_args["<person_first_name>"] = "Jane"
        person_args["<person_type>"] = "Staff"
        person_functions.create_person(person_args)

    def test_save_state(self):
        """
            Test saving data to database
        """

        # Test saving with default database
        person_functions.add_people_to_db()
        room_functions.add_rooms_to_db()
        people_in_db = amity_models.populate_people()
        rooms_in_db = amity_models.populate_rooms()

        self.assertTrue(
            os.path.exists("test_amity_db.sqlite"),
            msg="Default database not being created"
        )
        self.assertTrue(
            any(
                "Jane Doe" in person_names
                for person_names in
                [person.name for person in people_in_db]
            ),
            msg="People not being added to default database"
        )
        self.assertTrue(
            any(
                "Mordor" in room_names
                for room_names in
                [room.room_name for room in rooms_in_db]
            ),
            msg="Rooms not being added to default database"
        )

        # Test saving with user-defined database
        amity_models.change_db_path("test_my_db.sqlite")
        person_functions.add_people_to_db()
        room_functions.add_rooms_to_db()
        people_in_db = amity_models.populate_people()
        rooms_in_db = amity_models.populate_rooms()

        self.assertTrue(
            os.path.exists("test_my_db.sqlite"),
            msg="User-defined database not being created"
        )
        self.assertTrue(
            any(
                "John Doe" in person_names
                for person_names in
                [person.name for person in people_in_db]
            ),
            msg="People not being added to user-defined database"
        )
        self.assertTrue(
            any(
                "Go" in room_names
                for room_names in
                [room.room_name for room in rooms_in_db]
            ),
            msg="Rooms not being added to user-defined database"
        )

    def test_state_load(self):
        """
            Test loading data from database
        """

        # Test loading data from user-defined database
        people_in_db = amity_models.populate_people()
        rooms_in_db = amity_models.populate_rooms()

        self.assertTrue(
            any(
                "Jane Doe" in person_names
                for person_names in
                [person.name for person in people_in_db]
            ),
            msg="People not being added to user-defined database"
        )
        self.assertTrue(
            any(
                "Camelot" in room_names
                for room_names in
                [room.room_name for room in rooms_in_db]
            ),
            msg="Rooms not being added to user-defined database"
        )

    def tearDown(self):
        room_functions.current_rooms.rooms = {}
        room_functions.current_rooms.available_offices = []
        room_functions.current_rooms.available_livingspaces = []
        person_functions.people = {}


if __name__ == '__main__':
    unittest.main()
