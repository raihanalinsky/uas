from services.barang_service import BarangService


class BarangController:

    def __init__(self):

        self.service = BarangService()

    # ======================
    # Tambah Barang
    # ======================

    def tambah_barang(
        self,
        kode,
        nama,
        kategori,
        supplier,
        stok,
        harga
    ):

        return self.service.tambah_barang(
            kode,
            nama,
            kategori,
            supplier,
            stok,
            harga
        )

    # ======================
    # Hapus Barang
    # ======================

    def hapus_barang(self, kode):

        return self.service.hapus_barang(
            kode
        )

    # ======================
    # Barang Masuk
    # ======================

    def barang_masuk(
        self,
        kode,
        jumlah
    ):

        return self.service.barang_masuk(
            kode,
            jumlah
        )

    # ======================
    # Barang Keluar
    # ======================

    def barang_keluar(
        self,
        kode,
        jumlah
    ):

        return self.service.barang_keluar(
            kode,
            jumlah
        )

    # ======================
    # Cari Barang
    # ======================

    def cari_barang(
        self,
        keyword
    ):

        return self.service.cari_barang(
            keyword
        )

    # ======================
    # Semua Barang
    # ======================

    def get_all_barang(self):

        return self.service.get_all_barang()