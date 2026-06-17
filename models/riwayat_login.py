import pandas as pd
import os

from models.linked_list import LinkedList


class RiwayatLoginModel:

    FILE_PATH = "database/riwayat_login.csv"

    def __init__(self):

        os.makedirs("database", exist_ok=True)

        if not os.path.exists(self.FILE_PATH):

            df = pd.DataFrame(columns=["Username", "Role", "Login", "Logout"])

            df.to_csv(self.FILE_PATH, index=False)

    def load(self):

        ll = LinkedList()

        df = pd.read_csv(self.FILE_PATH, dtype=str)

        for _, row in df.iterrows():
            ll.append(row.to_dict())

        return ll

    def save(self, linked_list):

        pd.DataFrame(linked_list.to_list()).to_csv(self.FILE_PATH, index=False)

    def tambah_riwayat(self, data):

        df = pd.read_csv(self.FILE_PATH, dtype=str)

        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)

        df.to_csv(self.FILE_PATH, index=False)

    def update_logout(self, username):
        df = pd.read_csv(self.FILE_PATH, dtype=str)

        index = df[
            (df["Username"] == username) & (df["Logout"].isna() | (df["Logout"] == ""))
        ].index

        if len(index) > 0:
            df.loc[index[-1], "Logout"] = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")

            df.to_csv(self.FILE_PATH, index=False)
