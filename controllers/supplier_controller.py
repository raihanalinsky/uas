from services.supplier_service import SupplierService


class SupplierController:

    def __init__(self):

        self.service = SupplierService()

    def tambah_supplier(
        self,
        perusahaan,
        alamat,
        telpon,
        email,
        pic
    ):

        return self.service.tambah_supplier(
            perusahaan,
            alamat,
            telpon,
            email,
            pic
        )

    def get_all_supplier(self):

        return self.service.get_all_supplier()