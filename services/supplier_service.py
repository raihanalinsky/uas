from models.supplier_model import SupplierModel


class SupplierService:
    def __init__(self):
        self.model = SupplierModel()

    # ================
    # tambah supplier
    # ================

    def tambah_supplier(self, perusahaan, alamat, telpon, email, pic):
        pt = self.model.load()  # load data supplier

        # mengecek apakah semua data kosong atau tidak
        if perusahaan == "" or alamat == "" or telpon == "" or email == "" or pic == "":
            return False, "Semua Kolom Harus Diisi!"

        # menambahkan data
        pt.append(
            {
                "Nama Perusahaan": perusahaan,
                "Alamat": alamat,
                "No Telpon": telpon,
                "Email": email,
                "PIC": pic,
            }
        )

        # save data ke model
        self.model.save(pt)

        return True, "Supplier berhasil ditambahkan"

    # ================
    # hapus supplier
    # ================

    def hapus_supplier(self, perusahaan):
        pt = self.model.load()

        # mengecek apakah data = - atau tidak
        if perusahaan == "-":
            return False, "Pilihlah perusahaan/supplier dengan benar!!!!"

        hasil = pt.delete_by_key(
            "Nama Perusahaan", perusahaan
        )  # menghapus supplier yang sudah dipilih di node

        if not hasil:
            return False, "Gagal Menghapus Supplier"

        self.model.save(pt)
        return True, "Berhasil Menghapus Supplier"

    # ================
    # edit supplier
    # ================
    def edit_supplier(
        self, pilihan_perusahaan, nama_perusahaan, alamat, telpon, email, pic
    ):
        pt = self.model.load()
        if pilihan_perusahaan == "-":  # jika pilihan -
            return False, "Pilihlah supplier dengan benar!!"

        # mengecek apakah semuanya kosong atau tidak
        if (
            nama_perusahaan == ""
            and alamat == ""
            and telpon == ""
            and email == ""
            and pic == ""
        ):
            return False, "Minimal salah 1 harus diubah!"

        new_data = {}  # membuat dict baru

        # jika nama_perusahaan ada datanya / tidak kosong
        if nama_perusahaan != "":
            new_data["Nama Perusahaan"] = nama_perusahaan
        # jika alamat ada datanya / tidak kosong
        if alamat != "":
            new_data["Alamat"] = alamat
        # jika telepon ada datanya / tidak kosong
        if telpon != "":
            new_data["No Telpon"] = telpon
        # jika email ada datanya / tidak kosong
        if email != "":
            new_data["Email"] = email
        # jika pic ada datanya / tidak kosong
        if pic != "":
            new_data["PIC"] = pic

        # memperbarui data supplier pada linked list
        hasil = pt.update_by_key("Nama Perusahaan", pilihan_perusahaan, new_data)

        if not hasil:
            return False, "Gagal Mengedit Supplier!"

        self.model.save(pt)
        return True, "Berhasil Mengubah Supplier!"

    # ================
    # semua supplier
    # ================
    def get_all_supplier(self):
        # mengambil semua data supplier di node
        return self.model.load().to_list()
