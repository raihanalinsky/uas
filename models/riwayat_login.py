import pandas as pd
import os

from models.linked_list import LinkedList
from utils.path_helper import get_csv_path
from utils.path_helper import get_wib_time_now


class RiwayatLoginModel:
    FILE_PATH = get_csv_path("riwayat_login.csv")

    def __init__(self):
        if not os.path.exists(self.FILE_PATH):

            df = pd.DataFrame(columns=["Username", "Role", "Login", "Logout"])

            df.to_csv(self.FILE_PATH, index=False)

    # ====================
    # load riwayat login
    # ====================
    def load(self):
        ll = LinkedList()

        df = pd.read_csv(self.FILE_PATH, dtype=str)

        for _, row in df.iterrows():
            ll.append(row.to_dict())

        return ll

    # ====================
    # save riwayat login
    # ====================
    def save(self, linked_list):
        pd.DataFrame(linked_list.to_list()).to_csv(self.FILE_PATH, index=False)

    # ====================
    # tambah riwayat login
    # ====================
    def tambah_riwayat(self, data):
        df = pd.read_csv(self.FILE_PATH, dtype=str)

        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)

        df.to_csv(self.FILE_PATH, index=False)

    # ======================
    # update riwayat logout
    # ======================
    def update_logout(self, username):
        df = pd.read_csv(self.FILE_PATH, dtype=str)

        index = df[
            (df["Username"] == username) & (df["Logout"].isna() | (df["Logout"] == ""))
        ].index

        if len(index) > 0:
            df.loc[index[-1], "Logout"] = get_wib_time_now()

            df.to_csv(self.FILE_PATH, index=False)
