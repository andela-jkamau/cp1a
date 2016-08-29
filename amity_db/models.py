from peewee import *


db = SqliteDatabase('amitydb.db')


class BaseModel(Model):
    class Meta:
        database = db


class AmityRoom(BaseModel):
    room_name = TextField(unique=True)
    room_capacity = IntegerField()
    room_type = TextField()


class PersonDetails(BaseModel):
    person_id = IntegerField()
    name = TextField()
    person_type = TextField()
    office = TextField()
    living_space = TextField()
