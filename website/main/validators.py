from django.core.exceptions import ValidationError


class NumberValidator:
    ALLOWED_CHARS = "0123456789 "

    def __init__(self, message=None):
        self.message = message if message else "Enter numbers separated by space."

    def __call__(self, value):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, params={"value": value})
