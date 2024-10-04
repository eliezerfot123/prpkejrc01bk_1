from qaroni.database import Column, BaseModel, db, relationship, reference_col
import bson

class Books(BaseModel):
    """Books Model"""
    __tablename__ = "books"

    title = Column(db.String(80), nullable=False)
    description = Column(db.String(255), nullable=True)
    image_url = Column(db.String(255), nullable=True)
    category = Column(db.String(80), nullable=True)
    user_id = Column(db.String(80), nullable=True)

    def __init__(self):
        return

    def create(self, title="", description="", image_url="", category="", user_id=""):
        """Create a new book"""
        book = self.get_by_user_id_and_title(user_id, title)
        if book:
            return
        new_book = db.books.insert_one(
            {
                "title": title,
                "description": description,
                "image_url": image_url,
                "category": category,
                "user_id": user_id
            }
        )
        return self.get_by_id(new_book.inserted_id)


    def get_by_id(self, book_id):
        """Get a book by id"""
        book = db.books.find_one({"_id": bson.ObjectId(book_id)})
        if not book:
            return
        book["_id"] = str(book["_id"])
        return book

    def get_by_user_id(self, user_id):
        """Get all books created by a user"""
        books = db.books.find({"user_id": user_id})
        return [{**book, "_id": str(book["_id"])} for book in books]

    def get_by_category(self, category):
        """Get all books by category"""
        books = db.books.find({"category": category})
        return [book for book in books]

    def get_by_user_id_and_category(self, user_id, category):
        """Get all books by category for a particular user"""
        books = db.books.find({"user_id": user_id, "category": category})
        return [{**book, "_id": str(book["_id"])} for book in books]

    def get_by_user_id_and_title(self, user_id, title):
        """Get a book given its title and author"""
        book = db.books.find_one({"user_id": user_id, "title": title})
        if not book:
            return
        book["_id"] = str(book["_id"])
        return book

    def update(self, book_id, title="", description="", image_url="", category="", user_id=""):
        """Update a book"""
        data={}
        if title: data["title"]=title
        if description: data["description"]=description
        if image_url: data["image_url"]=image_url
        if category: data["category"]=category

        book = db.books.update_one(
            {"_id": bson.ObjectId(book_id)},
            {
                "$set": data
            }
        )
        book = self.get_by_id(book_id)
        return book

    def delete(self, book_id):
        """Delete a book"""
        book = db.books.delete_one({"_id": bson.ObjectId(book_id)})
        return book

    def delete_by_user_id(self, user_id):
        """Delete all books created by a user"""
        book = db.books.delete_many({"user_id": bson.ObjectId(user_id)})
        return book