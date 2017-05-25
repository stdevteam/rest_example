# Native Python Modules.
import datetime

# External Modules.
from rest_framework.serializers import ValidationError

# Django Modules.

# Project Modules.


def birthday_validation(value):
    today = datetime.date.today()
    if value > today:
        raise ValidationError('Birthday should be past date.')
    # They say that Methuselah lived 969 years, but we will use 100.
    if value < today - datetime.timedelta(days=(100 * 365)):
        raise ValidationError('Birthday should be in last 100 years.')
