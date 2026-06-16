import pandas as pd
import os
from utils.helper import base_dir_import


# ==========================
# Load Database CSV
# ==========================
def load_barang():
    if not os.path.exists(base_dir_import("barang.csv")):
        df = pd.DataFrame(columns=["Kode", "Nama Barang", "Kategori", "Stok", "Harga"])
        df.to_csv(base_dir_import("barang.csv"),index=False)
    return pd.read_csv(base_dir_import("barang.csv"))


def save_barang(data):
    data.to_csv(base_dir_import("barang.csv"),index=False)


def load_transaksi():
    if not os.path.exists(base_dir_import("transaksi.csv")):
        df = pd.DataFrame(columns=["Tanggal", "Jenis", "Kode", "Nama Barang", "Jumlah"])
        df.to_csv(base_dir_import("transaksi.csv"),index=False)
    return pd.read_csv(base_dir_import("transaksi.csv"))


def save_transaksi(data):
    data.to_csv(base_dir_import("transaksi.csv"),index=False)


def load_akun():
    if not os.path.exists(base_dir_import("akun.csv")):
        df = pd.DataFrame(columns=["Username", "Password", "Role"])
        df.to_csv(base_dir_import("akun.csv"),index=False)
    return pd.read_csv(base_dir_import("akun.csv"))


def save_akun(data):
    data.to_csv(base_dir_import("akun.csv"),index=False)


def load_riwayat_login():
    if not os.path.exists(base_dir_import("riwayat_login.csv")):
        df = pd.DataFrame(columns=["Username", "Role", "Login", "Logout"])
        df.to_csv(base_dir_import("riwayat_login.csv"),index=False)
    return pd.read_csv(base_dir_import("riwayat_login.csv"))


def save_riwayat_login(data):
    data.to_csv(base_dir_import("riwayat_login.csv"),index=False)


def load_supplier():
    if not os.path.exists(base_dir_import("supplier.csv")):
        df = pd.DataFrame(
            columns=["Nama Perusahaan", "Alamat", "No telpon", "Email", "PIC"]
        )
        df.to_csv(base_dir_import("supplier.csv"),index=False)

    return pd.read_csv(base_dir_import("supplier.csv"))


def save_supplier(data):
    data.to_csv(base_dir_import("supplier.csv"),index=False)
