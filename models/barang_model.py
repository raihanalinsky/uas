import pandas as pd
import os

from models.linked_list import LinkedList


class BarangModel:

    FILE_PATH = "database/barang.csv"

    def __init__(self):

        os.makedirs("database", exist_ok=True)

        if not os.path.exists(self.FILE_PATH):

            df = pd.DataFrame(
                columns=["Kode", "Nama Barang", "Kategori", "Supplier", "Stok", "Harga"]
            )

            df.to_csv(self.FILE_PATH, index=False)

    # ======================
    # Load CSV -> LinkedList
    # ======================

    def load(self):

        ll = LinkedList()

        df = pd.read_csv(self.FILE_PATH)

        for _, row in df.iterrows():
            ll.append(row.to_dict())

        return ll

    # ======================
    # Save LinkedList -> CSV
    # ======================

    def save(self, linked_list):

        pd.DataFrame(linked_list.to_list()).to_csv(self.FILE_PATH, index=False)
