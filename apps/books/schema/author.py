from marshmallow import Schema, fields


class AuthorSchema(Schema):
    name = fields.Str()

    class Meta:
        fields = ("name",)