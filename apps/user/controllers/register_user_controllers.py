from apps.user.services import CallUserRegisterServices


# register user views
class RegisterUserController:
    def __init__(self):
        self.call_user_services = CallUserRegisterServices()

    def execute(self, request_data):
        return self.call_user_services.execute(request_data)
