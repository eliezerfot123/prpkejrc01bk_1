from apps.books.dao.author import AuthorDAO


class CallAuthorServices:

    def __init__(self):
        self.dao = AuthorDAO()

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
