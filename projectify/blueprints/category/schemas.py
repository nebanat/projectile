from marshmallow import Schema, fields, validate, pre_load
from core.validation import CustomValidation


class CategorySchema(Schema):
    """
    Defines project schema with validations

    """
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True,
                      validate=[CustomValidation.must_not_be_blank, validate.Length(min=3, max=30)],
                      error_messages={'required': 'Category name field is required'})
    description = fields.Str(missing='', validate=[validate.Length(max=200)])

    slug = fields.Str(required=True,
                      error_messages={'required': 'Slug field cannot be empty'})

    created_on = fields.DateTime(required=True, dump_only=True)

    updated_on = fields.DateTime(required=True, dump_only=True)

    @pre_load()
    def slugify_name(self, data):
        data['slug'] = data['name'].lower().strip().replace(' ', '-')
        return data

    @pre_load()
    def name_to_lower(self, data):
        data['name'] = data['name'].lower()
        return data

    class Meta:
        strict = True
        many = True


