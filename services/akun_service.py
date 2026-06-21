from models.akun_model import AkunModel
from models.riwayat_login import RiwayatLoginModel


class AkunService:
    def __init__(self):
        self.model = AkunModel()
        self.riwayat_model = RiwayatLoginModel()

    # ============
    # tambah akun
    # ============
    def tambah_akun(self, username, password, role):
        akun = self.model.load()
        
        if username == "" or password == "":
            return False, "Username dan Password wajib diisi!"

        current = akun.head

        while current:

            if current.data["Username"] == username:

                return False, "Username sudah ada"

            current = current.next

        akun.append({"Username": username, "Password": password, "Role": role})

        self.model.save(akun)

        return True, "Akun berhasil dibuat"

    # ============
    # hapus akun
    # ============
    def hapus_akun(self, username):
        akun = self.model.load()

        hasil = akun.delete_by_key("Username", username)

        if not hasil:
            return False, "Akun tidak ditemukan"

        self.model.save(akun)

        return True, "Akun berhasil dihapus"

    # ============
    # semua akun
    # ============
    def get_all_akun(self):
        return self.model.load().to_list()

    # ==========================
    # semua riwayat login
    # ==========================
    def get_all_riwayat(self):
        return self.riwayat_model.load().to_list()
