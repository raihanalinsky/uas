from services.barang_service import BarangService


class BarangController:
    def __init__(self):
        self.service = BarangService()

    def tambah_barang(self, kode, nama, kategori, supplier, stok, harga):
        return self.service.tambah_barang(kode, nama, kategori, supplier, stok, harga)

    def hapus_barang(self, kode):
        return self.service.hapus_barang(kode)

    def edit_barang(self, barang_pilihan, kb, nbb, ktb, splr, sb, hb):
        return self.service.edit_barang(barang_pilihan, kb, nbb, ktb, splr, sb, hb)

    def barang_masuk(self, kode, jumlah):
        return self.service.barang_masuk(kode, jumlah)

    def barang_keluar(self, kode, jumlah):
        return self.service.barang_keluar(kode, jumlah)

    def cari_barang(self, keyword):
        return self.service.cari_barang(keyword)

    def get_all_barang(self):
        return self.service.get_all_barang()
