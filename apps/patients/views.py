# Native Python Modules.

# External Modules.

# Django Modules.

# Project Modules.
from .models import Patient
from .serializers import PatientSerializer
from core.mixins import AllMethodsViewSet


class PatientViewSet(AllMethodsViewSet):
    """
    CRUD endpoints for Patients.
    """
    model_name = "Patient"
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
