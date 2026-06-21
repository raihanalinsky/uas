import streamlit as st
import pandas as pd
import time

from utils.helper import is_admin


class SupplierView:
    def __init__(self, controller):
        self.controller = controller

    def render(self):
        st.title("Supplier")

        all_supplier = (
            self.controller.get_all_supplier()
        )  # ambil semua data supplier melewati controller

        st.dataframe(
            pd.DataFrame(all_supplier), use_container_width=True
        )  # menampilkan seluruh data supplier menggunakan pandas

        # membuat tabs
        tab1, tab2, tab3 = st.tabs(
            ["Tambah Supplier", "Edit Supplier", "Hapus Supplier"]
        )

        # tab untuk menambahkan supplier
        with tab1:
            if is_admin():
                with st.form("supplier", clear_on_submit=True):

                    perusahaan = st.text_input("Nama Perusahaan")

                    alamat = st.text_input("Alamat")

                    telpon = st.text_input("No Telpon")

                    email = st.text_input("Email")

                    pic = st.text_input("PIC")

                    if st.form_submit_button("Tambah Supplier"):
                        status, pesan = self.controller.tambah_supplier(
                            perusahaan, alamat, telpon, email, pic
                        )

                        # mengecek apakah berhasil menambahkan supplier atau tidak
                        if status:
                            st.success(pesan)
                            time.sleep(1)
                            st.rerun()
                        else:
                            st.error(pesan)

        # tab untuk mengedit supplier
        with tab2:
            if is_admin():
                with st.form("edit", clear_on_submit=True):
                    # untuk memilih supplier menggunakan selectbox
                    supplier = st.selectbox(
                        "Supplier", ["-"] + [x["Nama Perusahaan"] for x in all_supplier]
                    )

                    st.divider()  # garis

                    perusahaan = st.text_input("Nama Perusahaan")

                    alamat = st.text_input("Alamat")

                    telpon = st.text_input("No Telpon")

                    email = st.text_input("Email")

                    pic = st.text_input("PIC")

                    if st.form_submit_button("Submit"):

                        status, pesan = self.controller.edit_supplier(
                            supplier, perusahaan, alamat, telpon, email, pic
                        )

                        # mengecek apakah berhasil menambahkan supplier atau tidak
                        if status:
                            st.toast(pesan)
                            time.sleep(1)
                            st.rerun()
                        else:
                            st.toast(pesan)

        # tab untuk menghapus supplier
        with tab3:
            if is_admin():
                with st.form("hapus", clear_on_submit=True):

                    perusahaan = st.selectbox(
                        "Supplier", ["-"] + [x["Nama Perusahaan"] for x in all_supplier]
                    )

                    if st.form_submit_button("Submit"):
                        status, pesan = self.controller.hapus_supplier(perusahaan)

                        # mengecek apakah berhasil menambahkan supplier atau tidak
                        if status:
                            st.toast(pesan)
                            time.sleep(1)
                            st.rerun()
                        else:
                            st.toast(pesan)
