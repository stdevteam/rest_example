# -*- coding: utf-8 -*-

# Native Python Modules.
import json

# External Modules.
from rest_framework.response import Response


# Django Modules.

# Project Modules.


class RESTResponse(Response):
    """
    Basic settings for REST responses.
    """

    def get_model_name(self, obj):
        return getattr(obj, "model_name", obj.serializer_class.Meta.model.__name__)

    def init(self, status_code, kwargs):
        # This two lines should be the first lines.
        # As they are used in other called functions.
        self.obj = kwargs.pop("obj")
        self.method = kwargs.pop("method")
        mapping = {
            "{model}": self.get_model_name(self.obj),
            "{method}": self.method
        }
        message_pattern = self.message if hasattr(self,
                                                  "message") and self.message is not None else self.__class__.get_message(
            self.method)
        message = RESTResponse.construct_message(message_pattern, mapping)
        kwargs["data"] = RESTResponse.construct_data(message)
        kwargs["status"] = status_code

    @staticmethod
    def construct_data(message):
        return {
            "detail": message
        }

    @staticmethod
    def construct_message(message_pattern, mapping):
        for elem in mapping.keys():
            message_pattern = message_pattern.replace(elem, mapping[elem])
        return message_pattern


class Response201(RESTResponse):
    """
    Response extension for 201 status code responses to provide custom body.
    """
    message = "The new {model} has been {method}d."

    def __init__(self, *args, **kwargs):
        self.init(201, kwargs)
        super().__init__(*args, **kwargs)


class Response204(RESTResponse):
    """
    Response extension for 204 status code responses to provide custom body.
    """
    message = "The {model} has been deleted."

    def __init__(self, *args, **kwargs):
        self.init(204, kwargs)
        super().__init__(*args, **kwargs)


class Response401(RESTResponse):
    message = "The user is not authorized to perform this operation."

    def __init__(self, *args, **kwargs):
        kwargs["data"] = RESTResponse.construct_data(self.message)
        kwargs["status"] = 401
        super().__init__(*args, **kwargs)


class Response404(RESTResponse):
    """
    Response extension for 404 status code responses to provide custom body.
    """

    def __init__(self, *args, **kwargs):
        self.init(404, kwargs)
        super().__init__(*args, **kwargs)

    @classmethod
    def get_message(cls, method):
        if method == "destroy":
            return "The delete operation failed because the {model} does not exist."
        else:
            return "The requested {model} does not exist."


class Response422(RESTResponse):
    """
    Response extension for 422 status code responses to provide custom body.
    """
    message = "The {model} already exists and could therefore not be created again."

    def __init__(self, *args, **kwargs):
        self.init(422, kwargs)
        super().__init__(*args, **kwargs)


class Response412(RESTResponse):
    """
    Response extension for 412 status code responses to provide custom body.
    """
    message = "Precondition failed."

    def __init__(self, *args, **kwargs):
        self.message = kwargs.pop("message", self.message)
        kwargs["data"] = RESTResponse.construct_data(self.message)
        kwargs["status"] = 412
        super().__init__(*args, **kwargs)


class Response400(RESTResponse):
    """
    Response extension for 400 status code responses to provide custom body.
    """
    message = "Bad Request."

    def __init__(self, *args, **kwargs):
        self.message = kwargs.pop("data").decode("utf-8")
        kwargs["data"] = RESTResponse.construct_data(self.message)
        kwargs["status"] = 400
        super().__init__(*args, **kwargs)
        self.content = json.dumps(kwargs["data"])
