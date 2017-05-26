# Native Python Modules.
import datetime

# External Modules.
from rest_framework.serializers import ValidationError

# Django Modules.

# Project Modules.


def birthday_validation(value):
    """
    Validates birth date to be in past and not earlier than 100 years.

    :type value: datetime.date
    :param value: Birthday date.

    :raise ValidationError

    :rtype: void
    :return: void
    """
    today = datetime.date.today()
    if value > today:
        raise ValidationError('Birthday should be past date.')

    # They say that Methuselah lived 969 years, but we will use 100.
    if value < today - datetime.timedelta(days=(100 * 365)):
        raise ValidationError('Birthday should be in last 100 years.')
