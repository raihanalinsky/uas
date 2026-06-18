import streamlit as st
import pandas as pd
import time


class SupplierView:

    def __init__(self, controller):
        self.controller = controller

    def render(self):

        st.title("Supplier")

        all_supplier = self.controller.get_all_supplier()

        st.dataframe(pd.DataFrame(all_supplier), use_container_width=True)

        tab1, tab2, tab3 = st.tabs(
            ["Tambah Supplier", "Edit Supplier", "Hapus Supplier"]
        )

        with tab1:
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

                    if status:
                        st.success(pesan)
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error(pesan)
        with tab2:
            with st.form("edit", clear_on_submit=True):

                supplier = st.selectbox(
                    "Supplier", ["-"] + [x["Nama Perusahaan"] for x in all_supplier]
                )
                
                st.divider()

                perusahaan = st.text_input("Nama Perusahaan")

                alamat = st.text_input("Alamat")

                telpon = st.text_input("No Telpon")

                email = st.text_input("Email")

                pic = st.text_input("PIC")

                if st.form_submit_button("Submit"):

                    if supplier != "-":
                        status, pesan = self.controller.edit_supplier(
                            supplier, perusahaan, alamat, telpon, email, pic
                        )

                        if status:
                            st.toast(pesan)
                            time.sleep(1)
                            st.rerun()
                        else:
                            st.toast(pesan)
                    else:
                        st.toast("Pilihlah Supplier Dengan Benar!")

        with tab3:
            with st.form("hapus", clear_on_submit=True):

                supplier = st.selectbox(
                    "Supplier", ["-"] + [x["Nama Perusahaan"] for x in all_supplier]
                )
                if st.form_submit_button("Submit"):
                    if supplier != "-":
                        status, pesan = self.controller.hapus_supplier(supplier)

                        if status:
                            st.toast(pesan)
                            time.sleep(1)
                            st.rerun()
                        else:
                            st.toast(pesan)
                    else:
                        st.toast("Pilih Supplier Dengan Benar!")
