import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(
    page_title="Sistem Gudang",
    page_icon="📦",
    layout="wide"
)

# ==========================
# Load Database CSV
# ==========================

if not os.path.exists("barang.csv"):
    df = pd.DataFrame(columns=[
        "Kode",
        "Nama Barang",
        "Kategori",
        "Stok",
        "Harga"
    ])
    df.to_csv("barang.csv", index=False)

if not os.path.exists("transaksi.csv"):
    df = pd.DataFrame(columns=[
        "Tanggal",
        "Jenis",
        "Kode",
        "Nama Barang",
        "Jumlah"
    ])
    df.to_csv("transaksi.csv", index=False)


barang = pd.read_csv("barang.csv")
transaksi = pd.read_csv("transaksi.csv")

# ==========================
# Sidebar
# ==========================

menu = st.sidebar.selectbox(
    "Menu Gudang",
    [
        "Dashboard",
        "Data Barang",
        "Barang Masuk",
        "Barang Keluar",
        "Laporan"
    ]
)

# ==========================
# Dashboard
# ==========================

if menu == "Dashboard":

    st.title("📦 Dashboard Gudang")

    total_barang = len(barang)
    total_stok = barang["Stok"].sum()
    total_nilai = (barang["Stok"] * barang["Harga"]).sum()
    hampir_habis = len(barang[barang["Stok"] <= 5])

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Jenis Barang", total_barang)
    c2.metric("Total Stok", total_stok)
    c3.metric("Nilai Inventaris", f"Rp {total_nilai:,.0f}")
    c4.metric("Stok Menipis", hampir_habis)

    st.divider()

    st.subheader("Data Barang")

    st.dataframe(barang, use_container_width=True)

# ==========================
# Data Barang
# ==========================

elif menu == "Data Barang":

    st.title("📋 Master Barang")

    with st.form("input_barang"):

        kode = st.text_input("Kode Barang")
        nama = st.text_input("Nama Barang")
        kategori = st.selectbox(
            "Kategori",
            [
                "Elektronik",
                "ATK",
                "Makanan",
                "Minuman",
                "Lainnya"
            ]
        )

        stok = st.number_input(
            "Stok",
            min_value=0,
            step=1
        )

        harga = st.number_input(
            "Harga",
            min_value=0
        )

        simpan = st.form_submit_button("Tambah Barang")

        if simpan:

            data_baru = {
                "Kode": kode,
                "Nama Barang": nama,
                "Kategori": kategori,
                "Stok": stok,
                "Harga": harga
            }

            barang = pd.concat(
                [barang, pd.DataFrame([data_baru])],
                ignore_index=True
            )

            barang.to_csv(
                "barang.csv",
                index=False
            )

            st.success("Barang berhasil ditambahkan")

    st.divider()

    st.subheader("Daftar Barang")

    st.dataframe(
        barang,
        use_container_width=True
    )

    hapus = st.selectbox(
        "Pilih barang yang akan dihapus",
        ["-"] + list(barang["Kode"])
    )

    if st.button("Hapus Barang"):

        if hapus != "-":

            barang = barang[
                barang["Kode"] != hapus
            ]

            barang.to_csv(
                "barang.csv",
                index=False
            )

            st.success("Barang berhasil dihapus")

# ==========================
# Barang Masuk
# ==========================

elif menu == "Barang Masuk":

    st.title("📥 Barang Masuk")

    kode = st.selectbox(
        "Pilih Barang",
        barang["Kode"]
    )

    jumlah = st.number_input(
        "Jumlah",
        min_value=1,
        step=1
    )

    if st.button("Simpan"):

        idx = barang[
            barang["Kode"] == kode
        ].index[0]

        barang.loc[idx, "Stok"] += jumlah

        barang.to_csv(
            "barang.csv",
            index=False
        )

        data = {
            "Tanggal": datetime.now(),
            "Jenis": "Masuk",
            "Kode": kode,
            "Nama Barang": barang.loc[idx, "Nama Barang"],
            "Jumlah": jumlah
        }

        transaksi = pd.concat(
            [transaksi, pd.DataFrame([data])],
            ignore_index=True
        )

        transaksi.to_csv(
            "transaksi.csv",
            index=False
        )

        st.success("Barang masuk berhasil")

# ==========================
# Barang Keluar
# ==========================

elif menu == "Barang Keluar":

    st.title("📤 Barang Keluar")

    kode = st.selectbox(
        "Pilih Barang",
        barang["Kode"]
    )

    jumlah = st.number_input(
        "Jumlah Keluar",
        min_value=1,
        step=1
    )

    if st.button("Proses"):

        idx = barang[
            barang["Kode"] == kode
        ].index[0]

        if barang.loc[idx, "Stok"] >= jumlah:

            barang.loc[idx, "Stok"] -= jumlah

            barang.to_csv(
                "barang.csv",
                index=False
            )

            data = {
                "Tanggal": datetime.now(),
                "Jenis": "Keluar",
                "Kode": kode,
                "Nama Barang": barang.loc[idx, "Nama Barang"],
                "Jumlah": jumlah
            }

            transaksi = pd.concat(
                [transaksi, pd.DataFrame([data])],
                ignore_index=True
            )

            transaksi.to_csv(
                "transaksi.csv",
                index=False
            )

            st.success("Barang keluar berhasil")

        else:

            st.error("Stok tidak mencukupi")

# ==========================
# Laporan
# ==========================

elif menu == "Laporan":

    st.title("📊 Laporan Gudang")

    st.subheader("Inventaris")

    st.dataframe(
        barang,
        use_container_width=True
    )

    st.subheader("Riwayat Transaksi")

    st.dataframe(
        transaksi,
        use_container_width=True
    )

    csv = transaksi.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download Laporan CSV",
        data=csv,
        file_name="laporan_gudang.csv",
        mime="text/csv"
    )
