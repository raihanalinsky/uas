from services.akun_service import AkunService

class AkunController:

    def __init__(self):

        self.service = AkunService()

    # ======================
    # Tambah Akun
    # ======================

    def tambah_akun(
        self,
        username,
        password,
        role
    ):

        return self.service.tambah_akun(
            username,
            password,
            role
        )

    # ======================
    # Hapus Akun
    # ======================

    def hapus_akun(
        self,
        username
    ):

        return self.service.hapus_akun(
            username
        )

    # ======================
    # Semua Akun
    # ======================

    def get_all_akun(self):
        return self.service.get_all_akun()
    
    def get_all_riwayat(self):
        return self.service.get_all_riwayat()