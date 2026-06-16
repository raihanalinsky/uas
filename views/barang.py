import streamlit as st
import pandas as pd


class BarangView:

    def __init__(self, controller):
        self.controller = controller

    def render(self):

        st.title("Manajemen Barang")

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "Daftar Barang",
                "Tambah Barang",
                "Barang Masuk",
                "Barang Keluar"
            ]
        )

        with tab1:

            barang = self.controller.get_all_barang()

            st.dataframe(
                pd.DataFrame(barang),
                use_container_width=True
            )

        with tab2:

            with st.form("barang"):

                kode = st.text_input("Kode")
                nama = st.text_input("Nama Barang")
                kategori = st.text_input("Kategori")
                supplier = st.text_input("Supplier")

                stok = st.number_input(
                    "Stok",
                    min_value=0
                )

                harga = st.number_input(
                    "Harga",
                    min_value=0
                )

                submit = st.form_submit_button(
                    "Tambah"
                )

                if submit:

                    status, pesan = self.controller.tambah_barang(
                        kode,
                        nama,
                        kategori,
                        supplier,
                        stok,
                        harga
                    )

                    if status:
                        st.success(pesan)
                    else:
                        st.error(pesan)

        with tab3:

            kode = st.text_input(
                "Kode Barang Masuk"
            )

            jumlah = st.number_input(
                "Jumlah Masuk",
                min_value=1
            )

            if st.button("Proses Masuk"):

                status, pesan = self.controller.barang_masuk(
                    kode,
                    jumlah
                )

                if status:
                    st.success(pesan)
                else:
                    st.error(pesan)

        with tab4:

            kode = st.text_input(
                "Kode Barang Keluar"
            )

            jumlah = st.number_input(
                "Jumlah Keluar",
                min_value=1
            )

            if st.button("Proses Keluar"):

                status, pesan = self.controller.barang_keluar(
                    kode,
                    jumlah
                )

                if status:
                    st.success(pesan)
                else:
                    st.error(pesan)