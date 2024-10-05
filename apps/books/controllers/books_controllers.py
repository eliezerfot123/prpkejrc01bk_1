from apps.books.services.books_services import CallBooksServices


class BooksController:
    def __init__(self):
        self.call_books_services = CallBooksServices()

    def execute(self):
        return self.call_books_services.execute()

    def create_data(self, request_data):
        return self.call_books_services.create_data(request_data)

    def update_data(self, book_id, request_data):
        return self.call_books_services.update_data(book_id, request_data)

    def delete_data(self, book_id):
        return self.call_books_services.delete_data(book_id)

    def get_by_id(self, book_id):
        return self.call_books_services.get_by_id(book_id)

    def export_data(self):
        return self.call_books_services.export_data()
