"""
Package for the application.
"""
from django.db.models.query import QuerySet
from app.models import *
def Seed():
    Test = QuerySet
    Test = Person.objects
    for x in Test.all():      
        assert isinstance(x, Person) #Required for AutoComplete
        #x.delete()
        #x.save() 
        pass

    Test = Company.objects
    for x in Test.all():
        assert isinstance(x, Company) #Required for AutoComplete 
        #x.delete()
        #x.save() 
        pass

    Aaron = Person()
    Aaron.first_name = "Aaron"
    Aaron.last_name = "Campf"
    Aaron.save()

    AJP = Company()
    AJP.Name = "AJP Northwest"
    AJP.save()


#Seed()