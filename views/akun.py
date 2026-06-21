import streamlit as st
import pandas as pd
import time

from utils.helper import is_admin


class AkunView:
    def __init__(self, controller):
        self.controller = controller

    def render(self):
        if is_admin():  # mengecek apakah admin atau bukan
            st.title("Manajemen Akun")

            akun = (
                self.controller.get_all_akun()
            )  # meminta semua data akun dari akun service lewat akun controller

            username_list = [
                item["Username"] for item in self.controller.get_all_akun()
            ]

            st.dataframe(
                pd.DataFrame(akun), use_container_width=True
            )  # menampilkan seluruh data akun
            tab1, tab2, tab3, tab4 = st.tabs(  # membuat tabs
                ["Tambah Akun", "Hapus Akun", "Edit Akun", "Riwayat Login"]
            )

            # tab untuk menambahkan akun
            with tab1:
                with st.form("akun", clear_on_submit=True):
                    username = st.text_input("Username")

                    password = st.text_input("Password")

                    role = st.selectbox("Role", ["Admin", "User"])

                    if st.form_submit_button("Tambah Akun"):

                        status, pesan = self.controller.tambah_akun(
                            username, password, role
                        )

                        # menampilkan hasil
                        self.show_result(status, pesan)

            # tab untuk menghapus akun
            with tab2:
                hapus_akun = st.selectbox("Pilih Akun", ["-"] + username_list)

                if st.button("Hapus Akun"):
                    status, pesan = self.controller.hapus_akun(hapus_akun)

                    self.show_result(status, pesan)

            with tab3:
                with st.form("edit akun", clear_on_submit=True):
                    pilih_akun = st.selectbox("Pilih Akun", ["-"] + username_list)

                    st.divider()

                    username = st.text_input("Username")

                    password = st.text_input("Password")

                    role = st.selectbox("Role", ["-"] + ["Admin", "User"])

                    if st.form_submit_button("edit Akun"):

                        status, pesan = self.controller.edit_akun(
                            pilih_akun, username, password, role
                        )

                        # menampilkan hasil
                        self.show_result(status, pesan)

            with tab4:
                riwayat_list = self.controller.get_all_riwayat()

                st.dataframe(pd.DataFrame(riwayat_list[::-1]), use_container_width=True)

    def show_result(self, status, pesan):
        if status:
            st.toast(pesan)
            time.sleep(1)
            st.rerun()
        else:
            st.error(pesan)
