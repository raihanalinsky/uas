from models.akun_model import AkunModel
from models.riwayat_login import RiwayatLoginModel
from datetime import datetime

class AuthService:

    def __init__(self):
        self.model = AkunModel()
        self.riwayat_login = RiwayatLoginModel()

    def login(self, username, password):

        akun_list = self.model.get_all()

        current = akun_list.head

        while current:

            akun = current.data

            if (
                akun["Username"] == username
                and str(akun["Password"]) == str(password)
            ):

                data = {
                    "Username" : username,
                    "Login" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Logout" : ""
                }
                
                self.riwayat_login.tambah_riwayat(data)
                return True, akun

            current = current.next

        return False, None
    
    def logout(self, username):
        self.riwayat_login.update_logout(username)