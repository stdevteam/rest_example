# -*- coding: utf-8 -*-

# Native Python Modules.
import time
import os
import signal
import unittest
from urllib.parse import urlencode
import subprocess

# External Modules.
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

# Django Modules.
from django.contrib.auth.models import User
from django.test import TestCase
from django.conf import settings

# Project Modules.


class BaseTestCase(TestCase):
    """
    Base test case to provide more organized behavior.
    Extend all test cases from this one.
    """
    client = APIClient()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subprocesses = []

    def _provide_auth(self):
        if User.objects.count() == 0:
            user = User.objects.create_superuser("TESTUSER", "TEST.TEST@GMAIL.COM", "TESTPASSWORD")
        else:
            user = User.objects.first()
        try:
            self.token = Token.objects.get(user=user).key
        except:
            self.token = Token.objects.create(user=user).key
        return self.token

    def init_with_auth_token(self, kwargs):
        if "auth" not in kwargs or kwargs.pop("auth"):
            if not hasattr(self, "token"):
                if Token.objects.count() == 0:
                    self.token = self._provide_auth()
                else:
                    # Rare case.
                    self.token = Token.objects.all()[0].key
            kwargs['HTTP_AUTHORIZATION'] = "Token {0}".format(self.token)
        # Do not use this. As dict is mutable object.
        return kwargs

    def get(self, *args, **kwargs):
        """
        Simplifies usage of test.client.get.
        :see APIClienet.get
        """
        return self.client.get(*args, **self.init_with_auth_token(kwargs))

    def post(self, *args, **kwargs):
        """
        Simplifies usage of test.client.post.
        :see APIClinet.post
        """
        return self.client.post(*args, **self.init_with_auth_token(kwargs))

    def put(self, *args, **kwargs):
        """
        Simplifies usage of test.client.put.
        :see APIClinet.put
        """
        if len(args) > 0:
            args = args[:1] + (urlencode(args[1]),) + args[2:]
        return self.client.put(*args, content_type='application/x-www-form-urlencoded',
                               **self.init_with_auth_token(kwargs))

    def patch(self, *args, **kwargs):
        """
        Simplifies usage of test.client.patch.
        :see APIClient.patch
        """
        args = args[:1] + (urlencode(args[1]),) + args[2:]
        return self.client.patch(*args, content_type='application/x-www-form-urlencoded',
                                 **self.init_with_auth_token(kwargs))

    def delete(self, *args, **kwargs):
        """
        Simplifies usage of test.client.delete.
        :see APIClinet.delete
        """
        return self.client.delete(*args, **self.init_with_auth_token(kwargs))
