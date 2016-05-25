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

class Contact(models.Model):
    Name = models.CharField(max_length=30)
    Company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
    )

class Company(models.Model):
    """Represents a company"""

    Name = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    Zip = models.CharField(max_length=30)
    Phone = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)