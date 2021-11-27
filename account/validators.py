from django.core.exceptions import ValidationError
import re

def phone_validator(value):
    if not re.search(r'^\d{11}$', value):
        raise ValidationError('This is not a phone number buddy :/')
