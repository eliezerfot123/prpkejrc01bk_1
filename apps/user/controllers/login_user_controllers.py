from apps.user.services.login_user import CallUserLoginServices


class LoginUserController:
    def __init__(self):
        self.call_user_services = CallUserLoginServices()

    def execute(self, request_data):
        return self.call_user_services.login_user(request_data)
