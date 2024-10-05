from qaroni.database import Column, BaseModel, db, relationship, reference_col
import bson


authors = db.Table('authors',
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
)

class Book(BaseModel):
    """Books Model"""
    __tablename__ = "book"

    title = Column(db.String(80), nullable=False)
    description = Column(db.String(255), nullable=True)
    image_url = Column(db.String(255), nullable=True)
    category = Column(db.String(80), nullable=True)
    user_id = Column(db.String(80), nullable=True)
    authors = db.relationship('Author', secondary=authors, lazy='subquery',
        backref=db.backref('books', lazy=True))



    def __init__(self, title: str, description: str, image_url: str, category: str, user_id: str):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.category = category
        self.user_id = user_id

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image_url': self.image_url,
            'category': self.category,
            'user_id': self.user_id,
        }
    

class Author(BaseModel):
    """Author Model"""
    __tablename__ = "author"

    name = Column(db.String(80), nullable=False)

    def __init__(self, name: str):
        self.name = name
    
    def serialize(self):
        return {
            'id': self.id,
            'author': self.name,
        }
