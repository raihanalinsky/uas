from models.supplier_model import SupplierModel

class SupplierService:

    def __init__(self):

        self.model = SupplierModel()

    def tambah_supplier(
        self,
        perusahaan,
        alamat,
        telpon,
        email,
        pic
    ):

        supplier = self.model.load()

        supplier.append(
            {
                "Nama Perusahaan": perusahaan,
                "Alamat": alamat,
                "No Telpon": telpon,
                "Email": email,
                "PIC": pic
            }
        )

        self.model.save(supplier)

        return True, "Supplier berhasil ditambahkan"

    def get_all_supplier(self):

        return self.model.load().to_list()