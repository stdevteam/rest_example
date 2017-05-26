# -*- coding: utf-8 -*-

# Native Python Modules.
from random import randrange

# External Modules.

# Django Modules.

# Project Modules.
from core import responses
from core.tests import BaseTestCase


class ModelsBaseTestCase(BaseTestCase):
    """
    Base test cases for Models based resources.
    """

    email = "hovhannes.dabaghyan@gmail.com"
    username = "admin"
    password = "root"
    serializer = None

    def setUp(self):
        obj = self.create_model()
        self.to_update_id = obj.id
        self.deletable_id = obj.id
        self.patch_data = self.duplicated_data = self.generate_duplication_data(obj)

    def test_get_request_200(self):
        response = self.get(self.url)
        if len(response.data) > 0:
            self.assertSetEqual(set(self.get_dict.keys()), set(response.data[randrange(len(response.data))].keys()))
            for key, types in self.get_dict.items():
                if isinstance(types, (list, tuple)):
                    types = tuple(types)
                self.assertIsInstance(response.data[randrange(len(response.data))][key], types, key)
        self.assertEqual(response.status_code, 200)

    def test_get_request_404(self):
        not_existing_id = 0
        response = self.get("{0}/{1}".format(self.url, not_existing_id))
        self.assertEqual(response.data, self.supposed_data(responses.Response404, "retrieve"))
        self.assertEqual(response.status_code, 404)

    def test_post_request_201(self):
        response = self.post(self.url, self.post_data)
        self.assertEqual(response.data, self.supposed_data(responses.Response201, "create"))
        self.assertEqual(response.status_code, 201)

    def test_patch_request_201(self):
        response = self.patch("{0}/{1}".format(self.url, self.to_update_id), self.patch_data)
        self.assertEqual(response.data, self.supposed_data(responses.Response201, "update"))
        self.assertEqual(response.status_code, 201)

    def test_patch_request_404(self):
        response = self.patch(self.url + "/0", self.patch_data)
        self.assertEqual(response.data, self.supposed_data(responses.Response404, "update"))
        self.assertEqual(response.status_code, 404)

    def test_delete_request_204(self):
        response = self.delete("{0}/{1}".format(self.url, self.deletable_id), self.patch_data)
        self.assertEqual(response.data, self.supposed_data(responses.Response204, "destroy"))
        self.assertEqual(response.status_code, 204)

    def test_delete_request_404(self):
        response = self.delete(self.url + "/0")
        self.assertEqual(response.data, self.supposed_data(responses.Response404, "destroy"))
        self.assertEqual(response.status_code, 404)

    def supposed_data(self, response_cls, method):
        model_name = self.model_alias if hasattr(self, "model_alias") else self.model.__name__
        message_pattern = response_cls.message if hasattr(response_cls,
                                                          "message") and response_cls.message is not None else response_cls.get_message(
            method)
        mapping = {
            "{model}": model_name,
            "{method}": method
        }
        return responses.RESTResponse.construct_data(response_cls.construct_message(message_pattern, mapping))

    def generate_duplication_data(self, obj, serializer=None):
        """
        Generate duplicated body for object.
        """
        serializer = serializer if serializer else self.serializer
        if not serializer:
            raise Exception("No serializer is passed or has been set for test case class.")
        if not self.post_data:
            raise Exception("No post data.")
        returnable = dict()
        obj_values = dict()
        fields = self.serializer().get_fields()
        for field, value in fields.items():
            obj_values[field] = getattr(obj, value.source if value.source else field)

        for key, value in self.post_data.items():
            returnable[key] = obj_values[key]

        return returnable
