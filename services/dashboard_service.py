from models.barang_model import BarangModel
from models.supplier_model import SupplierModel

class DashboardService:

    def __init__(self):

        self.barang_model = BarangModel()
        self.supplier_model = SupplierModel()

    def get_dashboard_data(self):

        barang = self.barang_model.load()

        supplier = self.supplier_model.load()

        total_barang = 0
        total_stok = 0
        total_nilai = 0
        stok_menipis = 0

        current = barang.head

        while current:

            data = current.data

            total_barang += 1
            total_stok += int(data["Stok"])

            total_nilai += (
                int(data["Stok"])
                * float(data["Harga"])
            )

            if int(data["Stok"]) <= 5:

                stok_menipis += 1

            current = current.next

        total_supplier = len(
            supplier.to_list()
        )

        return {
            "total_barang": total_barang,
            "total_stok": total_stok,
            "total_nilai": total_nilai,
            "stok_menipis": stok_menipis,
            "total_supplier": total_supplier
        }