from models.supplier_model import SupplierModel


class SupplierService:

    def __init__(self):

        self.model = SupplierModel()

    def tambah_supplier(self, perusahaan, alamat, telpon, email, pic):

        pt = self.model.load()

        if perusahaan == "" or alamat == "" or telpon == "" or email == "" or pic == "":
            return False, "Semua Kolom Harus Diisi!"

        pt.append(
            {
                "Nama Perusahaan": perusahaan,
                "Alamat": alamat,
                "No Telpon": telpon,
                "Email": email,
                "PIC": pic,
            }
        )

        self.model.save(pt)

        return True, "Supplier berhasil ditambahkan"

    def hapus_supplier(self, perusahaan):
        pt = self.model.load()

        hasil = pt.delete_by_key("Nama Perusahaan", perusahaan)

        if not hasil:
            return False, "Gagal Menghapus Supplier"

        self.model.save(pt)
        return True, "Berhasil Menghapus Supplier"

    def edit_supplier(
        self, pilihan_perusahaan, nama_perusahaan, alamat, telpon, email, pic
    ):
        pt = self.model.load()

        if (
            nama_perusahaan == ""
            and alamat == ""
            and telpon == ""
            and email == ""
            and pic == ""
        ):
            return False, "Minimal salah 1 harus diubah!"

        new_data = {}

        if nama_perusahaan != "":
            new_data["Nama Perusahaan"] = nama_perusahaan
        if alamat != "":
            new_data["Alamat"] = alamat
        if telpon != "":
            new_data["No Telpon"] = telpon
        if email != "":
            new_data["Email"] = email
        if pic != "":
            new_data["PIC"] = pic

        hasil = pt.update_by_key("Nama Perusahaan", pilihan_perusahaan, new_data)
        
        if not hasil:
            return False, "Gagal Mengedit Supplier!"
        
        self.model.save(pt)
        return True, "Berhasil Mengubah Supplier!"

    def get_all_supplier(self):
        return self.model.load().to_list()
