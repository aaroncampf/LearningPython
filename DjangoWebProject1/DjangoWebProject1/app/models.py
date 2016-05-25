"""
Definition of models.
"""

from django.db import models
from django.db.models.query import QuerySet

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)



def Seed():
    Test = QuerySet
    Test = Person.objects
    for x in Test.all():
        pass

    Aaron = Person()
    Aaron.first_name = "Aaron"
    Aaron.last_name = "Campf"
    Aaron.save()


#Seed()
