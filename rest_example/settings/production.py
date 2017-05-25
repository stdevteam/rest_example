# Native Python Modules.

# External Modules.

# Django Modules.

# Project Modules.
from rest_example.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = True
THUMBNAIL_DEBUG = True

APPLICATION_PROTOCOL = "http"
RAW_HOST = "rest_example.dev"
BASE_URL = APPLICATION_PROTOCOL + "://" + RAW_HOST + "/"

ALLOWED_HOSTS = ['*', ]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rest_example',
        'USER': 'rest_example',
        'PASSWORD': 'gf741a9sd8kjno4u16ehb87rf',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + PROJECT_APPS

# Logging
ADMINS = (
    ('Hovhannes Dabaghyan', 'hovhannes.dabaghyan@gmail.com'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

# Media directory path, absolute.
MEDIA_PATH = "/var/www/rest_example/media/"

# Commented out as it will be specified dynamically.
# SWAGGER_SETTINGS['base_path'] = RAW_HOST + '/docs'

ROLLBAR = {
    'access_token': '3ba2c821b66b4ee5b9252618804d3d69',
    'environment': 'development' if DEBUG else 'production',
    'branch': 'master',
    'root': '/var/www/to/code/root',
}
