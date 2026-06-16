import pandas as pd
import os

from models.linked_list import LinkedList


class AkunModel:

    FILE_PATH = "database/akun.csv"

    def __init__(self):

        os.makedirs("database", exist_ok=True)

        if not os.path.exists(self.FILE_PATH):

            df = pd.DataFrame(
                columns=[
                    "Username",
                    "Password",
                    "Role"
                ]
            )

            df.to_csv(
                self.FILE_PATH,
                index=False
            )

    def load(self):

        ll = LinkedList()

        df = pd.read_csv(
            self.FILE_PATH,
            dtype=str
        )

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

    def get_all(self):
        return self.load()