# Native Python Modules.

# External Modules.

# Django Modules.
from django.db import models

# Project Modules.


class Patient(models.Model):
    GENDERS = (
        (0, 'Male',),
        (1, 'Female',),
        (2, 'Other',),
    )
    gender = models.SmallIntegerField(choices=GENDERS)
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True, null=False)
    birthdate = models.DateField(null=False)
