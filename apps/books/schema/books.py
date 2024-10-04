from marshmallow import Schema, fields

class BooksSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    image_url = fields.Str()
    category = fields.Str()
    user_id = fields.Str()
    authors = fields.List(fields.Str())

    class Meta:
        fields = ("title", "description", "image_url", "category", "user_id", "authors")
        
