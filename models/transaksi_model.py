import pandas as pd
import os

from models.linked_list import LinkedList
from utils.path_helper import get_csv_path


class TransaksiModel:
    FILE_PATH = get_csv_path("transaksi.csv")

    def __init__(self):
        if not os.path.exists(self.FILE_PATH):

            df = pd.DataFrame(
                columns=["Tanggal", "Jenis", "Kode", "Nama Barang", "Jumlah"]
            )

            df.to_csv(self.FILE_PATH, index=False)

    # ======================
    # load transaksi
    # ======================
    def load(self):
        ll = LinkedList()

        df = pd.read_csv(self.FILE_PATH, dtype=str)

        for _, row in df.iterrows():
            ll.append(row.to_dict())

        return ll

    # ======================
    # save transaksi
    # ======================
    def save(self, linked_list):
        pd.DataFrame(linked_list.to_list()).to_csv(self.FILE_PATH, index=False)

    # ======================
    # tambah transaksi
    # ======================
    def tambah_transaksi(self, data):
        df = pd.read_csv(self.FILE_PATH)

        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)

        df.to_csv(self.FILE_PATH, index=False)
