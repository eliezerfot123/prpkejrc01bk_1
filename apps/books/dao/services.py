from qaroni.database import db
from sqlalchemy.orm import Session
from apps.books.models import Book, Author
from apps.books.schema.books import BooksSchema

class BooksDAO:
    def __init__(self):
        self.model = Book

    def get_all(self):
        """Get all books"""
        books = self.model.query.all()
        if not books:
            return False

        # Serialize the query results
        schema = BooksSchema(many=True)
        books = schema.dump(books)

        return books

    def create(self, **kwargs):
        """Create a new book"""
        import ipdb; ipdb.set_trace()
        pop_author = kwargs.pop('authors')
        schema = BooksSchema()
        book = self.model(
            title=schema.load(kwargs)['title'],
            description=schema.load(kwargs)['description'],
            image_url=schema.load(kwargs)['image_url'],
            category=schema.load(kwargs)['category'],
            user_id=schema.load(kwargs)['user_id'],
        )

        # save m2m authors 
        for author in pop_author:
            author = Author.query.filter_by(id=author).first()
            book.authors.append(author)
        
        # save book
        db.session.add(book)
        db.session.commit()
        return book
    
    def update(self, id: int, **kwargs) -> bool:
        """Update a book with a particular id, and edit the authors"""
        book = self.model.query.get(id)
        if book is None:
            return False

        authors = kwargs.pop('authors', [])

        for key, value in kwargs.items():
            setattr(book, key, value)

        # Update the authors
        book.authors = [Author.query.get(author_id) for author_id in authors]

        book.save()
        return True

    
    def get_by_id(self, id):
        """Get book by id"""
        book = self.model.query.filter_by(id=id).first()
        if not book:
            return False
        schema = BooksSchema()
        book = schema.dump(book)
        return book
    
    def delete(self, id):
        """Delete a book by id"""
        book = self.model.query.get(id)
        if not book:
            return False
        db.session.delete(book)
        db.session.commit()
        return True