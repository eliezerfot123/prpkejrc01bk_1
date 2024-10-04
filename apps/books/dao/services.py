from qaroni.database import db
from sqlalchemy.orm import Session
from apps.books.models import Books
from apps.books.schema.books import BooksSchema

class BooksDAO:
    def __init__(self):
        self.model = Books

    def get_all(self):
        """Get all books"""
        books = self.model.query.all()
        if not books:
            return False

        # Serialize the query results
        schema = BooksSchema(many=True)
        books = schema.dump(books)

        return books
