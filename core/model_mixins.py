# -*- coding: utf-8 -*-

# Native Python Modules.

# External Modules.
from rest_framework import viewsets, mixins

# Django Modules.
from django.http import Http404
from django.db.utils import IntegrityError

# Project Modules.
from .responses import Response201, Response204, Response400, Response404, Response422
from core.rest_exceptions import Exception422


class ListModelMixin(mixins.ListModelMixin):
    """
    ListModelMixin Wrapper to provide custom responses.
    """
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RetrieveModelMixin(mixins.RetrieveModelMixin):
    """
    RetrieveModelMixin Wrapper to provide custom responses.
    """
    def retrieve(self, request, *args, **kwargs):
        try:
            response = super().retrieve(request, *args, **kwargs)
        except Http404 as e:
            return Response404(obj=self, method="retrieve")
        return response


class CreateModelMixin(mixins.CreateModelMixin):
    """
    CreateModelMixin Wrapper to provide custom responses.
    """

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
        except (Http404, IntegrityError, Exception422) as e:
            if isinstance(e, Http404):
                return Response404(obj=self, method="create")
            if isinstance(e, (IntegrityError, Exception422)):
                return Response422(obj=self, method="create")
        return Response201(obj=self, method="create")


class UpdateModelMixin(mixins.UpdateModelMixin):
    """
    UpdateModelMixin Wrapper to provide custom responses.
    """

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        try:
            response = super().update(request, *args, **kwargs)
        except (Http404, IntegrityError) as e:
            if isinstance(e, Http404):
                return Response404(obj=self, method="update")
            if isinstance(e, IntegrityError):
                return Response422(obj=self, method="update")
        return Response201(obj=self, method="update")


class DestroyModelMixin(mixins.DestroyModelMixin):
    """
    DestroyModelMixin Wrapper to provide custom responses.
    """

    def destroy(self, request, *args, **kwargs):
        try:
            response = super().destroy(request, *args, **kwargs)
        except Http404 as e:
            if isinstance(e, Http404):
                return Response404(obj=self, method="destroy")
        return Response204(obj=self, method="destroy")
