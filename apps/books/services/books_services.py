from apps.books.dao import BooksDAO


class CallBooksServices:
    def __init__(self):
        self.dao = BooksDAO()

    def execute(self):
        return self.dao.get_all()

    def create_data(self, request_data):
        return self.dao.create(**request_data)

    def update_data(self, id, request_data):
        return self.dao.update(id, **request_data)

    def delete_data(self, id):
        return self.dao.delete(id)

    def get_by_id(self, id):
        return self.dao.get_by_id(id)

    def export_data(self):
        return self.dao.export_data()
