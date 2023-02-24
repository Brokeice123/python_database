# install peewee
from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "keith.db"))


# creating our first table.

class User(Model):
    name = CharField()
    email = CharField()
    password = CharField()

    class Meta:
        database = db


User.create_table(fail_silently=True)
