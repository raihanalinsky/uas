import pandas as pd
import os

from models.linked_list import LinkedList


class TransaksiModel:

    FILE_PATH = "database/transaksi.csv"

    def __init__(self):

        os.makedirs("database", exist_ok=True)

        if not os.path.exists(self.FILE_PATH):

            df = pd.DataFrame(
                columns=[
                    "Tanggal",
                    "Jenis",
                    "Kode",
                    "Nama Barang",
                    "Jumlah"
                ]
            )

            df.to_csv(
                self.FILE_PATH,
                index=False
            )

    def load(self):

        ll = LinkedList()

        df = pd.read_csv(self.FILE_PATH)

        for _, row in df.iterrows():
            ll.append(row.to_dict())

        return ll

    def save(self, linked_list):

        pd.DataFrame(
            linked_list.to_list()
        ).to_csv(
            self.FILE_PATH,
            index=False
        )

    # ======================
    # Tambah Transaksi
    # ======================

    def tambah_transaksi(self, data):

        df = pd.read_csv(self.FILE_PATH)

        df = pd.concat(
            [df, pd.DataFrame([data])],
            ignore_index=True
        )

        df.to_csv(
            self.FILE_PATH,
            index=False
        )