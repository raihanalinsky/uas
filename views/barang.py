import streamlit as st
import pandas as pd


class BarangView:

    def __init__(self, controller):
        self.controller = controller

    def render(self):

        st.title("Manajemen Barang")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["Daftar Barang", "Tambah Barang", "Barang Masuk", "Barang Keluar"]
        )

        with tab1:

            barang = self.controller.get_all_barang()

            st.dataframe(pd.DataFrame(barang), use_container_width=True)

        with tab2:
            if st.session_state.role != "Admin":
                st.error("Hanya Admin Yang dapat mengakses Fitur Ini!")
            else:
                with st.form("barang", clear_on_submit=True):

                    kode = st.text_input("Kode")
                    nama = st.text_input("Nama Barang")
                    kategori = st.text_input("Kategori")
                    supplier = st.text_input("Supplier")

                    stok = st.number_input("Stok", min_value=0)

                    harga = st.number_input("Harga", min_value=0)

                    submit = st.form_submit_button("Tambah")

                    if submit:

                        status, pesan = self.controller.tambah_barang(
                            kode, nama, kategori, supplier, stok, harga
                        )

                        if status:
                            st.success(pesan)
                        else:
                            st.error(pesan)

        with tab3:
            barang = self.controller.get_all_barang()
            with st.form("masuk", clear_on_submit=True):
                opsi = [f"{item['Kode']} - {item['Nama Barang']}" for item in barang]
                kode = st.selectbox("Kode Barang Masuk", ["-"] + opsi)

                jumlah = st.number_input("Jumlah Masuk", min_value=1)

                if st.form_submit_button("Proses Masuk"):
                    kode_barang = kode.split("-")[0]
                    status, pesan = self.controller.barang_masuk(kode_barang, jumlah)

                    if status:
                        st.success(pesan)
                    else:
                        st.error(pesan)

        with tab4:
            with st.form("keluar", clear_on_submit=True):
                opsi = [f"{item['Kode']} - {item['Nama Barang']}" for item in barang]
                kode = st.selectbox("Kode Barang Keluar", ["-"] + opsi)

                jumlah = st.number_input("Jumlah Keluar", min_value=1)

                if st.form_submit_button("Proses Keluar"):
                    kode_barang = kode.split("-")[0]
                    status, pesan = self.controller.barang_keluar(kode_barang, jumlah)

                    if status:
                        st.success(pesan)
                    else:
                        st.error(pesan)
