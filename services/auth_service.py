from models.akun_model import AkunModel

class AuthService:

    def __init__(self):
        self.model = AkunModel()

    def login(self, username, password):

        akun_list = self.model.get_all()

        current = akun_list.head

        while current:

            akun = current.data

            if (
                akun["Username"] == username
                and str(akun["Password"]) == str(password)
            ):
                return True, akun

            current = current.next

        return False, None