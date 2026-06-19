from services.laporan_service import LaporanService
import pandas as pd


class LaporanController:
    def __init__(self):
        self.service = LaporanService()

    def get_laporan_transaksi(self):
        return self.service.get_laporan_transaksi()

    def total_barang_masuk(self):
        return self.service.total_barang_masuk()

    def total_barang_keluar(self):
        return self.service.total_barang_keluar()
    
    def get_all_laporan_bulanan(self):
        return self.service.laporan_per_bulan()