# Native Python Modules.

# External Modules.
from rest_framework import viewsets, mixins

# Django Modules.

# Project Modules.
from .models import Patient
from .serializers import PatientSerializer


class PatientViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
