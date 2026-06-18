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

    def tambah_barang(self, kode, nama, kategori, supplier, stok, harga):

        barang = self.barang_model.load()
        if (
            kode == ""
            or nama == ""
            or kategori == ""
            or supplier == ""
            or stok == ""
            or harga == ""
        ):
            return False, "Semua Kolom Harus Diisi!"
        if barang.find(kode):

            return False, "Kode barang sudah ada"

        barang.append(
            {
                "Kode": kode,
                "Nama Barang": nama,
                "Kategori": kategori,
                "Supplier": supplier,
                "Stok": stok,
                "Harga": harga,
            }
        )

        self.barang_model.save(barang)

        return True, "Barang berhasil ditambahkan"

    # ======================
    # Hapus Barang
    # ======================

    def hapus_barang(self, kode):

        barang = self.barang_model.load()

        hasil = barang.delete_by_key("Kode", kode)

        if not hasil:
            return False, "Barang tidak ditemukan"

        self.barang_model.save(barang)

        return True, "Barang berhasil dihapus"

    def edit_barang(
        self,
        barang_pilihan,
        kode_baru,
        nama_barang_baru,
        kategori_baru,
        stok_baru,
        harga_baru,
    ):
        all_barang = self.barang_model.load()

        if barang_pilihan == "-" or barang_pilihan == "":
            return False, "Pilih Barang Dengan Benar"
        if (
            kode_baru == ""
            and nama_barang_baru == ""
            and kategori_baru == ""
            and (stok_baru == "" or stok_baru == 0)
            and (harga_baru == "" or harga_baru == 0)
        ):
            return False, "Minimal 1 kolom harus diisi!"

        new_data = {}

        if kode_baru != "":
            new_data["Kode"] = kode_baru
            
        if nama_barang_baru != "":
            new_data["Nama Barang"] = nama_barang_baru
            
        if kategori_baru != "":
            new_data["Kategori"] = kategori_baru
            
        if stok_baru != 0:
            new_data["Stok"] = stok_baru
            
        if harga_baru != 0:
            new_data["Harga"] = harga_baru

        hasil = all_barang.update_by_key("Kode", barang_pilihan, new_data)

        if not hasil:
            return False, "Gagal Mengedit Barang"

        self.barang_model.save(all_barang)
        return True, "Berhasil Mengubah Barang"

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

    def barang_masuk(self, kode, jumlah):

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
                "Jumlah": jumlah,
            }
        )

        return True, "Barang masuk berhasil"

    # ======================
    # Barang Keluar
    # ======================

    def barang_keluar(self, kode, jumlah):

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
                "Jumlah": jumlah,
            }
        )

        return True, "Barang keluar berhasil"

    # ======================
    # Ambil Semua Barang
    # ======================

    def get_all_barang(self):

        return self.barang_model.load().to_list()
