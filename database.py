from peewee import *


dbase = SqliteDatabase("Movies.db")
class Movie(Model):
  img_url = CharField(max_length=1000,unique=True)
  name = CharField(max_length=50,unique=True)
  url = CharField(max_length=1000,unique=True)
  description = CharField(max_length=5000)
  
  class Meta:
    database = dbase
    table_name = "movies"
dbase.create_tables([Movie])