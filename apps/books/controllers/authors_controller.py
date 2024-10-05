from apps.books.services.author_services import CallAuthorServices

class AuthorsController:
    def __init__(self):
        self.call_author_services = CallAuthorServices()

    def get_all(self):
        return self.call_author_services.execute()
    
    def create_data(self, request_data):
        return self.call_author_services.create_data(request_data)

    def update_data(self, author_id, request_data):
        return self.call_author_services.update_data(author_id, request_data)

    def delete_data(self, author_id):
        return self.call_author_services.delete_data(author_id)

    def get_by_id(self, author_id):
        return self.call_author_services.get_by_id(author_id)