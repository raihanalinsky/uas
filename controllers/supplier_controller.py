from services.supplier_service import SupplierService


class SupplierController:

    def __init__(self):
        self.service = SupplierService()

    def tambah_supplier(self, perusahaan, alamat, telpon, email, pic):
        return self.service.tambah_supplier(perusahaan, alamat, telpon, email, pic)
    
    def hapus_supplier(self, nama_perusahaan):
        return self.service.hapus_supplier(nama_perusahaan)

    def get_all_supplier(self):
        return self.service.get_all_supplier()

    def edit_supplier(self, pilihan_perusahaan, perusahaan, alamat, telpon, email, pic):
        return self.service.edit_supplier(pilihan_perusahaan, perusahaan, alamat, telpon, email, pic)