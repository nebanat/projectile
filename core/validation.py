from marshmallow import ValidationError
# custom validator


class CustomValidation:
    @classmethod
    def must_not_be_blank(cls, data):
        if not data:
            raise ValidationError("This field must not be empty")
