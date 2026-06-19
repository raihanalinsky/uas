from models.transaksi_model import TransaksiModel
import pandas as pd


class LaporanService:
    def __init__(self):
        self.model = TransaksiModel()

    # ========================
    # semua laporan transaksi
    # ========================

    def get_laporan_transaksi(self):
        return self.model.load().to_list()

    # ========================
    # total barang yang masuk
    # ========================
    def total_barang_masuk(self):
        transaksi = self.model.load()

        total = 0

        current = transaksi.head

        while current:

            if current.data["Jenis"] == "Masuk":

                total += int(current.data["Jumlah"])

            current = current.next

        return total

    # ========================
    # total barang yang keluar
    # ========================
    def total_barang_keluar(self):

        transaksi = self.model.load()

        total = 0

        current = transaksi.head

        while current:

            if current.data["Jenis"] == "Keluar":

                total += int(current.data["Jumlah"])

            current = current.next

        return total

    # ===================
    # laporan per bulan
    # ===================
    def laporan_per_bulan(self):
        transaksi = self.model.load()
        
        data_bulanan = {}
        
        current = transaksi.head
        
        while current:
            bulan = current.data["Tanggal"][:7]
            jenis = current.data["Jenis"]
            jumlah = int(current.data["Jumlah"])
            
            if bulan not in data_bulanan:
                data_bulanan[bulan] = {
                    "Masuk" : 0,
                    "Keluar" : 0
                }

            data_bulanan[bulan][jenis] += jumlah
            
            current = current.next
        return pd.DataFrame([
            {
                "Bulan" : bulan,
                "Masuk" : nilai["Masuk"],
                "Keluar" : nilai["Keluar"]
            }
            for bulan, nilai in data_bulanan.items()
        ])