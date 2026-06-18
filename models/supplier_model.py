import pandas as pd
import os

from models.linked_list import LinkedList
from utils.path_helper import get_csv_path


class SupplierModel:

    FILE_PATH = get_csv_path("supplier.csv")

    def __init__(self):
        if not os.path.exists(self.FILE_PATH):

            df = pd.DataFrame(
                columns=["Nama Perusahaan", "Alamat", "No Telpon", "Email", "PIC"]
            )

            df.to_csv(self.FILE_PATH, index=False)

    # ==============
    # load supplier
    # ==============

    def load(self):
        ll = LinkedList()

        df = pd.read_csv(self.FILE_PATH, dtype=str)

        for _, row in df.iterrows():
            ll.append(row.to_dict())

        return ll

    # ==============
    # save supplier
    # ==============
    def save(self, linked_list):
        pd.DataFrame(linked_list.to_list()).to_csv(self.FILE_PATH, index=False)
