import streamlit as st
import pandas as pd
import time


class BarangView:

    def __init__(self, barang_controller, supplier_controller):
        self.barang_controller = barang_controller
        self.supplier_controller = supplier_controller

    def render(self):
        all_barang = self.barang_controller.get_all_barang()
        all_supplier = self.supplier_controller.get_all_supplier()

        st.title("Manajemen Barang")
        st.dataframe(pd.DataFrame(all_barang), use_container_width=True)

        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "Tambah Barang",
                "Hapus Barang",
                "Edit Barang",
                "Barang Masuk",
                "Barang Keluar",
            ]
        )

        with tab1:
            if st.session_state.role != "Admin":
                st.error("Hanya Admin Yang dapat mengakses Fitur Ini!")
            else:
                with st.form("barang", clear_on_submit=True):

                    kode_barang = st.text_input("Kode")
                    nama_barang = st.text_input("Nama Barang")
                    kategori_barang = st.text_input("Kategori")
                    supplier = st.selectbox(
                        "Pilih Supplier",
                        ["-"] + [x["Nama Perusahaan"] for x in all_supplier],
                    )

                    stok_barang = st.number_input("Stok", min_value=0)

                    harga_barang = st.number_input("Harga", min_value=0)

                    if st.form_submit_button("Tambah"):
                        if supplier != "-":
                            status, pesan = self.barang_controller.tambah_barang(
                                kode_barang,
                                nama_barang,
                                kategori_barang,
                                supplier,
                                stok_barang,
                                harga_barang,
                            )

                            if status:
                                st.toast(pesan)
                                time.sleep(1)
                                st.rerun()
                            else:
                                st.toast(pesan)
                        else:
                            st.toast("Pilih Supplier dengan benar!")

        with tab2:
            opsi_barang = [
                f"{item['Kode']}-{item['Nama Barang']}" for item in all_barang
            ]

            kode = st.selectbox("Barang Yang Ingin Di Hapus", ["-"] + opsi_barang)

            if st.button("Hapus"):
                if kode != "-":
                    hasil_kode = kode.split("-")[0]

                    status, pesan = self.barang_controller.hapus_barang(hasil_kode)

                    if status:
                        st.toast(pesan)
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.toast(pesan)
                else:
                    st.toast("Pilih Barang dengan Benar!")

        with tab3:
            with st.form("Edit Barang", clear_on_submit=True):
                kode_barang = st.selectbox("Pilih Barang", ["-"] + opsi_barang)
                st.divider()

                kode_baru = st.text_input("Kode Baru")
                nama_barang_baru = st.text_input("Nama Barang Baru")
                kategori_baru = st.text_input("Kategori Baru")
                stok_baru = st.number_input("Stok Baru", min_value=0)
                harga_baru = st.number_input("Harga Baru", min_value=0)

                if st.form_submit_button("Submit"):
                    hasil_kode = kode_barang.split("-")[0]
                    status, pesan = self.barang_controller.edit_barang(
                        hasil_kode,
                        kode_baru,
                        nama_barang_baru,
                        kategori_baru,
                        stok_baru,
                        harga_baru,
                    )
                    if status:
                        st.toast(pesan)
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.toast(pesan)

        with tab4:
            with st.form("masuk", clear_on_submit=True):
                kode = st.selectbox("Kode Barang Masuk", ["-"] + opsi_barang)

                jumlah = st.number_input("Jumlah Masuk", min_value=1)

                if st.form_submit_button("Proses Masuk"):
                    kode_barang = kode.split("-")[0]
                    status, pesan = self.barang_controller.barang_masuk(
                        kode_barang, jumlah
                    )

                    if status:
                        st.success(pesan)
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error(pesan)

        with tab5:
            with st.form("keluar", clear_on_submit=True):
                kode = st.selectbox("Kode Barang Keluar", ["-"] + opsi_barang)

                jumlah = st.number_input("Jumlah Keluar", min_value=1)

                if st.form_submit_button("Proses Keluar"):
                    kode_barang = kode.split("-")[0]
                    status, pesan = self.barang_controller.barang_keluar(
                        kode_barang, jumlah
                    )

                    if status:
                        st.success(pesan)
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error(pesan)
