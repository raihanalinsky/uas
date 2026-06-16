import streamlit as st
import pandas as pd


class SupplierView:

    def __init__(self, controller):
        self.controller = controller

    def render(self):

        st.title("Supplier")

        supplier = self.controller.get_all_supplier()

        st.dataframe(
            pd.DataFrame(supplier),
            use_container_width=True
        )

        with st.form("supplier"):

            perusahaan = st.text_input(
                "Nama Perusahaan"
            )

            alamat = st.text_input(
                "Alamat"
            )

            telpon = st.text_input(
                "No Telpon"
            )

            email = st.text_input(
                "Email"
            )

            pic = st.text_input(
                "PIC"
            )

            submit = st.form_submit_button(
                "Tambah Supplier"
            )

            if submit:

                status, pesan = self.controller.tambah_supplier(
                    perusahaan,
                    alamat,
                    telpon,
                    email,
                    pic
                )

                if status:
                    st.success(pesan)
                else:
                    st.error(pesan)