from apps.books.models import Author
from apps.books.schema.author import AuthorSchema
from qaroni.database import db


class AuthorDAO:
    def __init__(self):
        self.model = Author

    def get_all(self):
        """Get all authors"""
        schema = AuthorSchema(many=True)
        authors = schema.dump(self.model.query.all())

        return authors

    def create(self, **kwargs):
        """Create a new author"""
        # save author
        import ipdb

        ipdb.set_trace()
        author = self.model(name=kwargs["name"])
        db.session.add(author)
        db.session.commit()
        return author

    def update(self, id, **kwargs):
        """Update a author with a particular id"""
        author = self.model.query.get(id)
        if author is None:
            return False
        for key, value in kwargs.items():
            setattr(author, key, value)
        db.session.commit()
        return author

    def delete(self, id):
        """Delete a author with a particular id"""
        author = self.model.query.get(id)
        if not author:
            return False
        db.session.delete(author)
        db.session.commit()
        return True

    def get_by_id(self, id):
        """Get author by id"""
        author = self.model.query.get(id)
        if not author:
            return False
        schema = AuthorSchema()
        author = schema.dump(author)
        return author
