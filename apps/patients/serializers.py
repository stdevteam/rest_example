# Native Python Modules.

# External Modules.
from rest_framework import serializers as rest_serializers
from rest_framework.validators import UniqueValidator

# Django Modules.

# Project Modules.
from core import validators
from .models import Patient


class PatientSerializer(rest_serializers.HyperlinkedModelSerializer):
    gender = rest_serializers.ChoiceField(choices=Patient.GENDERS, required=True)
    firstname = rest_serializers.CharField(max_length=255, required=True)
    lastname = rest_serializers.CharField(max_length=255, required=True)
    email = rest_serializers.EmailField(required=True, validators=[UniqueValidator(Patient.objects.all())])
    birthdate = rest_serializers.DateField(required=True, validators=[validators.birthday_validation])

    class Meta:
        model = Patient
        fields = (
            'gender',
            'firstname',
            'lastname',
            'email',
            'birthdate',
        )
