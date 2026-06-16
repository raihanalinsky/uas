from models.transaksi_model import TransaksiModel

class LaporanService:

    def __init__(self):

        self.model = TransaksiModel()

    def get_laporan_transaksi(self):

        return self.model.load().to_list()

    def total_barang_masuk(self):

        transaksi = self.model.load()

        total = 0

        current = transaksi.head

        while current:

            if current.data["Jenis"] == "Masuk":

                total += int(current.data["Jumlah"])

            current = current.next

        return total

    def total_barang_keluar(self):

        transaksi = self.model.load()

        total = 0

        current = transaksi.head

        while current:

            if current.data["Jenis"] == "Keluar":

                total += int(current.data["Jumlah"])

            current = current.next

        return total