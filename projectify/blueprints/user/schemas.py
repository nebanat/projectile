from webargs import fields, validate

# parsed schema for user registration
user_register_args = {
    'username': fields.Str(required=True,
                           validate=validate.Length(min=5)),
    'email': fields.Str(required=True,
                        validate=validate.Email()),
    'password': fields.Str(required=True,
                           validate=validate.Length(min=6))
}

