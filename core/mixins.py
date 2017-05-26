# -*- coding: utf-8 -*-

# Native Python Modules.

# External Modules.
from rest_framework import viewsets

# Django Modules.

# Project Modules.
from .model_mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin


class BaseViewSet(viewsets.GenericViewSet):
    """
    General settings of ViewSets.
    """
    pass


class AllMethodsViewSet(BaseViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin,
                        UpdateModelMixin, DestroyModelMixin):
    """
    Grouping all(list, retrieve, create, update, destroy) available ModelMixins.
    """
    allowed_methods = ("GET", "POST", "PUT", "PATCH", "DELETE",)
