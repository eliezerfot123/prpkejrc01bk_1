from apps.user.dao import LoginUserDAO


class CallUserLoginServices:
    def __init__(self):
        self.dao = LoginUserDAO()

    def login_user(self, request_data):
        return self.dao.login_user(request_data)
