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

if not os.path.exists("akun.csv"):
    df = pd.DataFrame(columns=[
        "Username",
        "Password",
    ])
    df.to_csv("akun.csv", index=False)
    
if not os.path.exists("riwayat_login.csv"):
    df = pd.DataFrame(columns=[
        "Username",
        "Role",
        "Login",
        "Logout"
    ])
    df.to_csv("riwayat_login.csv", index=False)

barang = pd.read_csv("barang.csv")
transaksi = pd.read_csv("transaksi.csv")
akun = pd.read_csv("akun.csv", dtype=str)
riwayat_login = pd.read_csv("riwayat_login.csv", dtype=str)

# ========================
# Login
# ========================

if "login" not in st.session_state :
    st.session_state.login = False
    st.session_state.role = None
    st.session_state.username = None
    st.session_state.waktu_login = None
    
if not st.session_state.login:
    st.title("Login")
    
    username = st.text_input("Username :")
    password = st.text_input("Password :", type="password")
    
    if st.button("login"):
        
        login_berhasil = False
        
        for _, user in akun.iterrows():
            if username == user["Username"] and password == str(user["Password"]):
                login_berhasil = True
                st.session_state.role = user["Role"]
                st.session_state.username = user["Username"]
                st.session_state.waktu_login = datetime.now()           
                break
            
        if login_berhasil:
                st.session_state.login = True
                st.rerun()
        else:
            st.error("Gagal Login")
            
            
# ==========================
# Sidebar
# ==========================
else:

    st.sidebar.title("PT. Warehause Fams")
    
    menu = st.sidebar.selectbox(
        "Menu Gudang",
        [
            "Dashboard",
            "Data Barang",
            "Barang Masuk",
            "Barang Keluar",
            "Laporan",
            "Akun"
        ]
    )
    
    # ==========================
    # Logout
    # ==========================
    
    if st.sidebar.button("Logout"):
        st.session_state.login = False
        st.session_state.role = None
        
        logout_time = {
            "Username" : st.session_state.username,
            "Role" : st.session_state.role,
            "Login" : st.session_state.waktu_login,
            "Logout" : datetime.now()
            }
                        
        riwayat_login = pd.concat(
            [riwayat_login, pd.DataFrame([logout_time])],
            ignore_index=True
       )
                        
        riwayat_login.to_csv(
            "riwayat_login.csv",
            index=False
        )            
           
        st.rerun()
    
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

    
    
    #========================
    # Akun Khusus Admin
    #========================
    elif menu == "Akun":
        if st.session_state.role != "Admin":
            st.error("Anda Bukan Admin")
        else:
            
            st.title("Akun")

            st.subheader("Daftar Akun")

            st.dataframe(
                akun,
                use_container_width=True
            )

            st.subheader("Riwayat Login")

            st.dataframe(
                riwayat_login,
                use_container_width=True
            )

            csv = riwayat_login.to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(
                label="Download Laporan CSV",
                data=csv,
                file_name="riwayat_login.csv",
                mime="text/csv"
            )