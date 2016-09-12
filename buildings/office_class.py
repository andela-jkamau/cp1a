from .room_class import Room
from .room_functions import current_rooms


class Office(Room):

    """
            This class extends the `Room` class
                by specifying it is an office
                and giving it a `people_allocated` property.
            people_allocated = A list of the identifiers
                of the people allocated to a room.
    """

    def __init__(self, people_allocated=None, **kwargs):
        super().__init__(**kwargs)
        self.people_allocated = people_allocated or []

    def add_person_to_room(self, person_id):
        if len(self.people_allocated) < self.room_capacity:
            self.people_allocated.append(person_id)
        if len(self.people_allocated) == self.room_capacity:
            current_rooms.available_offices.remove(self.room_name)

    def remove_person_from_room(self, person_id):
        self.people_allocated.remove(person_id)
