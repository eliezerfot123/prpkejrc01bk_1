from apps.books.dao import BooksDAO


class CallBooksServices:
    def __init__(self):
        self.dao = BooksDAO()

    def execute(self):
        return self.dao.get_all()