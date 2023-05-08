from marshmallow import fields, validate

from app.extensions import ma


class UserSchema(ma.Schema):
    id = fields.String(dump_only=True)
    email = fields.Email(required=True, validate=validate.Length(max=64))
    password = fields.String(
        required=True, load_only=True, validate=validate.Length(min=6, max=64))

    class Meta:
        ordered = True
