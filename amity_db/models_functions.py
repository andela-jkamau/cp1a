from .models import *


class db_operations(object):
    """
    This class holds all functionality to work with the db
    """

    def __init__(self, db_path):
        self.db_path = db_path

    def get_rooms(self):
        return AmityRoom.select()

    def get_people(self):
        return PersonDetails.select
