from models.barang_model import BarangModel
from models.transaksi_model import TransaksiModel

from datetime import datetime

class BarangService:

    def __init__(self):

        self.barang_model = BarangModel()
        self.transaksi_model = TransaksiModel()

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

        barang = self.barang_model.load()

        if barang.find(kode):

            return False, "Kode barang sudah ada"

        barang.append(
            {
                "Kode": kode,
                "Nama Barang": nama,
                "Kategori": kategori,
                "Supplier": supplier,
                "Stok": stok,
                "Harga": harga
            }
        )

        self.barang_model.save(barang)

        return True, "Barang berhasil ditambahkan"

    # ======================
    # Hapus Barang
    # ======================

    def hapus_barang(self, kode):

        barang = self.barang_model.load()

        hasil = barang.delete(kode)

        if not hasil:
            return False, "Barang tidak ditemukan"

        self.barang_model.save(barang)

        return True, "Barang berhasil dihapus"

    # ======================
    # Cari Barang
    # ======================

    def cari_barang(self, keyword):

        barang = self.barang_model.load()

        hasil = []

        current = barang.head

        while current:

            if keyword.lower() in current.data["Nama Barang"].lower():

                hasil.append(current.data)

            current = current.next

        return hasil

    # ======================
    # Barang Masuk
    # ======================

    def barang_masuk(
        self,
        kode,
        jumlah
    ):

        barang = self.barang_model.load()

        node = barang.find(kode)

        if not node:

            return False, "Barang tidak ditemukan"

        node.data["Stok"] = int(node.data["Stok"]) + jumlah

        self.barang_model.save(barang)

        self.transaksi_model.tambah_transaksi(
            {
                "Tanggal": datetime.now(),
                "Jenis": "Masuk",
                "Kode": kode,
                "Nama Barang": node.data["Nama Barang"],
                "Jumlah": jumlah
            }
        )

        return True, "Barang masuk berhasil"

    # ======================
    # Barang Keluar
    # ======================

    def barang_keluar(
        self,
        kode,
        jumlah
    ):

        barang = self.barang_model.load()

        node = barang.find(kode)

        if not node:

            return False, "Barang tidak ditemukan"

        stok = int(node.data["Stok"])

        if stok < jumlah:

            return False, "Stok tidak mencukupi"

        node.data["Stok"] = stok - jumlah

        self.barang_model.save(barang)

        self.transaksi_model.tambah_transaksi(
            {
                "Tanggal": datetime.now(),
                "Jenis": "Keluar",
                "Kode": kode,
                "Nama Barang": node.data["Nama Barang"],
                "Jumlah": jumlah
            }
        )

        return True, "Barang keluar berhasil"

    # ======================
    # Ambil Semua Barang
    # ======================

    def get_all_barang(self):

        return self.barang_model.load().to_list()