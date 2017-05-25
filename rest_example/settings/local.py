# Native Python Modules.

# External Modules.

# Django Modules.

# Project Modules.
from rest_example.settings.base import *

DEBUG = True
THUMBNAIL_DEBUG = True
THUMBNAIL_PRESERVE_FORMAT = True

APPLICATION_PROTOCOL = "http"
RAW_HOST = "127.0.0.1:8000"
BASE_URL = APPLICATION_PROTOCOL + "://" + RAW_HOST + "/"

ALLOWED_HOSTS = ['*', ]

THIRD_PARTY_APPS += [
    'debug_toolbar',
    'django_extensions',
]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + PROJECT_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rest_example',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': ''
    }
}


# we can receive email messages using this command python -m smtpd -n -c DebuggingServer localhost:1025

# Media directory path, absolute.
MEDIA_PATH = "/var/www/rest_example/media/"

# SWAGGER_SETTINGS['base_path'] = RAW_HOST + '/docs'
