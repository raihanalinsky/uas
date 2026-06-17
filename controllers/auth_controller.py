from services.auth_service import AuthService


class AuthController:

    def __init__(self):
        self.service = AuthService()

    def login(self, username, password):

        return self.service.login(username, password)

    def logout(self, username):
        self.service.logout(username)
