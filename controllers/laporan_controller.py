from services.laporan_service import LaporanService


class LaporanController:

    def __init__(self):

        self.service = LaporanService()

    # ======================
    # Semua Transaksi
    # ======================

    def get_laporan_transaksi(self):

        return self.service.get_laporan_transaksi()

    # ======================
    # Total Barang Masuk
    # ======================

    def total_barang_masuk(self):

        return self.service.total_barang_masuk()

    # ======================
    # Total Barang Keluar
    # ======================

    def total_barang_keluar(self):

        return self.service.total_barang_keluar()