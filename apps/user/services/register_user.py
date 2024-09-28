from apps.user.dao import CreateUserDAO

class CallUserRegisterServices:

    def __init__(self):
        self.dao = CreateUserDAO()

    def execute(self, request_data):
        return self.dao.create(**request_data)