from models.akun_model import AkunModel
from models.riwayat_login import RiwayatLoginModel
from utils.helper import get_wib_time_now


class AuthService:
    def __init__(self):
        self.model = AkunModel()
        self.riwayat_login = RiwayatLoginModel()

    # ==================
    # autentikasi login
    # ==================
    def login(self, username, password):

        akun_list = self.model.load()

        current = akun_list.head

        while current:

            akun = current.data

            if akun["Username"] == username and str(akun["Password"]) == str(password):

                data = {
                    "Username": username,
                    "Login": get_wib_time_now(),
                    "Logout": "",
                }

                self.riwayat_login.tambah_riwayat(data)
                return True, akun

            current = current.next

        return False, None

    # ====================================================
    # jika logout maka akan memperbarui data waktu logout
    # ====================================================
    def logout(self, username):
        self.riwayat_login.update_logout(username)
