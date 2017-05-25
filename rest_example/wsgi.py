# Native Python Modules.
import os

# External Modules.

# Django Modules.
from django.core.wsgi import get_wsgi_application

# Project Modules.


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rest_example.settings.production")

application = get_wsgi_application()
