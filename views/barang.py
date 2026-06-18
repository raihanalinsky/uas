import streamlit as st
import pandas as pd
import time

from utils.helper import is_admin, get_barang_kode


class BarangView:
    def __init__(self, barang_controller, supplier_controller):
        self.barang_controller = barang_controller
        self.supplier_controller = supplier_controller

    def render(self):
        all_barang = (
            self.barang_controller.get_all_barang()
        )  # mengambil semua data barang
        all_supplier = (
            self.supplier_controller.get_all_supplier()
        )  # mengambil semua data supplier

        opsi_barang = [f"{item['Kode']}-{item['Nama Barang']}" for item in all_barang]

        st.title("Manajemen Barang")
        st.dataframe(
            pd.DataFrame(all_barang), use_container_width=True
        )  # menampilkan seluruh data barang

        # membuat 5 tabs untuk beberapa fitur
        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "Tambah Barang",
                "Hapus Barang",
                "Edit Barang",
                "Barang Masuk",
                "Barang Keluar",
            ]
        )

        # tab untuk menambahkan barang
        with tab1:
            if is_admin():  # mengecek apakah role admin atau bukan
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
                        status, pesan = self.barang_controller.tambah_barang(
                            kode_barang,
                            nama_barang,
                            kategori_barang,
                            supplier,
                            stok_barang,
                            harga_barang,
                        )

                        # mengecek apakah berhasil menambahkan barang atau tidak
                        self.show_result(status, pesan)
        # tab untuk menghapus barang
        with tab2:
            if is_admin():  # apakah admin atau bukan
                kode = st.selectbox("Barang Yang Ingin Di Hapus", ["-"] + opsi_barang)

                if st.button("Hapus"):
                    status, pesan = self.barang_controller.hapus_barang(
                        get_barang_kode(kode)  # hanya mengambil kode barang
                    )

                    self.show_result(status, pesan)

        # tab untuk mengedit barang
        with tab3:
            if is_admin():  # mengecek apakah admin atau bukan
                with st.form("Edit Barang", clear_on_submit=True):
                    kode_barang = st.selectbox("Pilih Barang", ["-"] + opsi_barang)

                    st.divider()

                    kode_baru = st.text_input("Kode Baru")

                    nama_barang_baru = st.text_input("Nama Barang Baru")

                    kategori_baru = st.text_input("Kategori Baru")

                    stok_baru = st.number_input("Stok Baru", min_value=0)

                    harga_baru = st.number_input("Harga Baru", min_value=0)

                    if st.form_submit_button("Submit"):

                        # mengirim data ke service untuk di cek apakah sudah sesuai atau belum
                        status, pesan = self.barang_controller.edit_barang(
                            get_barang_kode(kode_barang),
                            kode_baru,
                            nama_barang_baru,
                            kategori_baru,
                            stok_baru,
                            harga_baru,
                        )

                        # mengecek apakah berhasil mengedit barang atau tidak
                        self.show_result(status, pesan)

        # tab untuk barang masuk
        with tab4:
            with st.form("masuk", clear_on_submit=True):
                kode = st.selectbox("Kode Barang Masuk", ["-"] + opsi_barang)

                jumlah = st.number_input("Jumlah Masuk", min_value=1)

                if st.form_submit_button("Proses Masuk"):
                    status, pesan = self.barang_controller.barang_masuk(
                        get_barang_kode(kode), jumlah
                    )

                    # mengecek apakah berhasil atau tidak
                    self.show_result(status, pesan)
        with tab5:
            with st.form("keluar", clear_on_submit=True):
                kode = st.selectbox("Kode Barang Keluar", ["-"] + opsi_barang)

                jumlah = st.number_input("Jumlah Keluar", min_value=1)

                if st.form_submit_button("Proses Keluar"):
                    status, pesan = self.barang_controller.barang_keluar(
                        get_barang_kode(kode), jumlah
                    )

                    # mengecek apakah berhasil atau tidak
                    self.show_result(status, pesan)

    # template untuk status dan pesan
    def show_result(self, status, pesan):
        if status:
            st.toast(pesan)
            time.sleep(1)
            st.rerun()
        else:
            st.error(pesan)
