from apps.books.services.books_services import CallBooksServices

class BooksController:
    def __init__(self):
        self.call_books_services = CallBooksServices()

    def execute(self):
        return self.call_books_services.execute()