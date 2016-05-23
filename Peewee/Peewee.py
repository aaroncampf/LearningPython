from peewee import *

db = SqliteDatabase('Database\people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database



class Company(Model):
    """Represents a company"""

    Name = CharField()
    Address = CharField()
    City = CharField()
    State = CharField()
    Zip = CharField()
    Phone = CharField()
    Email = CharField()
    #Contacts = [Contact]
    class Meta:
        database = db # this model uses the "people.db" database

db.connect()
#db.create_tables([Person, Pet, Company])

AJP = Company.get(Company.Name == "Aaron Campf")

Test = Company()
Test.Name = "Aaron Campf"
Test.Address = ""
Test.City = "Portland"
Test.State = "OR"
Test.Zip = "97034"
Test.Phone = "(503) 929-8022"
Test.Email = "test@gmail.com"

Test.save()