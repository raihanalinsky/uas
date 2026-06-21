from services.akun_service import AkunService


class AkunController:
    def __init__(self):
        self.service = AkunService()

    def tambah_akun(self, username, password, role):
        return self.service.tambah_akun(username, password, role)

    def hapus_akun(self, username):
        return self.service.hapus_akun(username)
    
    def edit_akun(self, pilih_akun, username, password, role):
        return self.service.edit_akun(pilih_akun, username, password, role)

    def get_all_akun(self):
        return self.service.get_all_akun()

    def get_all_riwayat(self):
        return self.service.get_all_riwayat()
