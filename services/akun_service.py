from models.akun_model import AkunModel

class AkunService:

    def __init__(self):

        self.model = AkunModel()

    def tambah_akun(
        self,
        username,
        password,
        role
    ):

        akun = self.model.load()

        current = akun.head

        while current:

            if current.data["Username"] == username:

                return False, "Username sudah ada"

            current = current.next

        akun.append(
            {
                "Username": username,
                "Password": password,
                "Role": role
            }
        )

        self.model.save(akun)

        return True, "Akun berhasil dibuat"

    def hapus_akun(self, username):

        akun = self.model.load()

        hasil = akun.delete_by_username(username)

        if not hasil:

            return False, "Akun tidak ditemukan"

        self.model.save(akun)

        return True, "Akun berhasil dihapus"

    def get_all_akun(self):

        return self.model.load().to_list()