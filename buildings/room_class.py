class Room(object):

    """
            This class extends the Amity class.
            It extends `Amity` class with `room_capacity`,
                `room_name` and `room_type` properties.
            room_capacity = The capacity of a room:
                4 for living spaces and 6 for offices
            room_name = The room's name
            room_type = The type of the room: office or living space
    """

    def __init__(
            self, room_capacity, room_name,
            room_type, people_allocated=None
    ):
        self.room_capacity = room_capacity
        self.room_name = room_name
        self.room_type = room_type
        self.people_allocated = people_allocated or []

    def remove_person_from_room(self, person_id):
        self.people_allocated.remove(person_id)
