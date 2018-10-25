from django.core import validators
from django.utils.translation import gettext_lazy as _

class FriendValidator(validators.RegexValidator):
    regex = r'^[\w]+$'
    message = _(
        'Enter a Friendly Name. This value may contain only letters,and '
        'numbers'
    )
    flags = 0