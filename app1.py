import os
from io import BytesIO
from datetime import datetime

import pandas as pd
import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Warehouse Control Center",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================
# FILE PATH
# =========================
ITEM_FILE = "barang.csv"
SUPPLIER_FILE = "supplier.csv"
TRANSACTION_FILE = "transaksi.csv"

# =========================
# INITIAL DATA
# =========================
ITEM_COLUMNS = [
    "Kode", "Nama Barang", "Kategori", "Lokasi Rak",
    "Stok", "Minimum Stok", "Harga", "Deskripsi"
]

SUPPLIER_COLUMNS = [
    "ID", "Nama Supplier", "Telepon", "Alamat"
]

TRANSACTION_COLUMNS = [
    "Waktu", "Jenis", "Kode", "Nama Barang", "Jumlah", "Petugas", "Keterangan"
]


def ensure_file(path: str, columns: list):
    if not os.path.exists(path):
        pd.DataFrame(columns=columns).to_csv(path, index=False)


def safe_read_csv(path: str, columns: list) -> pd.DataFrame:
    ensure_file(path, columns)
    df = pd.read_csv(path)
    for col in columns:
        if col not in df.columns:
            df[col] = ""
    return df[columns]


def save_csv(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)


def load_all_data():
    items = safe_read_csv(ITEM_FILE, ITEM_COLUMNS)
    suppliers = safe_read_csv(SUPPLIER_FILE, SUPPLIER_COLUMNS)
    transactions = safe_read_csv(TRANSACTION_FILE, TRANSACTION_COLUMNS)

    # numeric clean-up
    for col in ["Stok", "Minimum Stok"]:
        if col in items.columns:
            items[col] = pd.to_numeric(items[col], errors="coerce").fillna(0).astype(int)

    if "Harga" in items.columns:
        items["Harga"] = pd.to_numeric(items["Harga"], errors="coerce").fillna(0).astype(float)

    if "Jumlah" in transactions.columns:
        transactions["Jumlah"] = pd.to_numeric(transactions["Jumlah"], errors="coerce").fillna(0).astype(int)

    return items, suppliers, transactions


def next_id(df: pd.DataFrame, prefix: str) -> str:
    if df.empty:
        return f"{prefix}001"
    existing = []
    for x in df.iloc[:, 0].astype(str).tolist():
        digits = "".join([c for c in x if c.isdigit()])
        if digits:
            existing.append(int(digits))
    num = max(existing) + 1 if existing else 1
    return f"{prefix}{num:03d}"


def status_stok(stok: int, minimum: int) -> str:
    if stok <= 0:
        return "Habis"
    elif stok <= minimum:
        return "Rendah"
    return "Aman"


def rupiah(x):
    try:
        return f"Rp {x:,.0f}".replace(",", ".")
    except:
        return "Rp 0"


def add_transaction(df: pd.DataFrame, jenis: str, kode: str, nama: str, jumlah: int, petugas: str, keterangan: str):
    new_row = pd.DataFrame([{
        "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Jenis": jenis,
        "Kode": kode,
        "Nama Barang": nama,
        "Jumlah": int(jumlah),
        "Petugas": petugas,
        "Keterangan": keterangan
    }])
    df = pd.concat([df, new_row], ignore_index=True)
    save_csv(df, TRANSACTION_FILE)
    return df


def inject_css():
    st.markdown(
        """
        <style>
            .stApp {
                background: linear-gradient(180deg, #f8fbff 0%, #f3f7fb 100%);
            }

            section[data-testid="stSidebar"] {
                background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
            }

            section[data-testid="stSidebar"] * {
                color: #ffffff !important;
            }

            .hero {
                padding: 22px 24px;
                border-radius: 22px;
                background: linear-gradient(135deg, #0f172a 0%, #1e293b 55%, #334155 100%);
                color: white;
                box-shadow: 0 10px 30px rgba(15, 23, 42, 0.18);
                margin-bottom: 18px;
            }

            .hero h1 {
                margin: 0;
                font-size: 34px;
                line-height: 1.1;
            }

            .hero p {
                margin: 8px 0 0 0;
                opacity: 0.9;
                font-size: 15px;
            }

            .card {
                background: white;
                padding: 18px 18px;
                border-radius: 20px;
                box-shadow: 0 8px 25px rgba(15, 23, 42, 0.06);
                border: 1px solid rgba(148, 163, 184, 0.18);
            }

            .mini-label {
                font-size: 12px;
                color: #64748b;
                margin-bottom: 6px;
            }

            .mini-value {
                font-size: 24px;
                font-weight: 700;
                color: #0f172a;
                margin-bottom: 2px;
            }

            .mini-note {
                font-size: 12px;
                color: #94a3b8;
            }

            div[data-testid="stMetric"] {
                background: white;
                border: 1px solid rgba(148, 163, 184, 0.18);
                padding: 14px;
                border-radius: 18px;
                box-shadow: 0 8px 25px rgba(15, 23, 42, 0.05);
            }

            .block-title {
                font-size: 18px;
                font-weight: 700;
                color: #0f172a;
                margin: 6px 0 10px 0;
            }

            .stButton > button {
                border-radius: 12px;
                padding: 0.55rem 1rem;
                border: none;
                background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
                color: white;
                font-weight: 600;
            }

            .stDownloadButton > button {
                border-radius: 12px;
                border: none;
                font-weight: 600;
            }

            .stTextInput > div > div > input,
            .stNumberInput > div > div > input,
            .stSelectbox > div > div,
            .stTextArea > div > div > textarea {
                border-radius: 12px !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


def render_hero():
    st.markdown(
        """
        <div class="hero">
            <h1>📦 Warehouse Control Center</h1>
            <p>Dashboard gudang modern untuk kelola stok, barang masuk/keluar, supplier, dan laporan.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_stat_cards(items: pd.DataFrame):
    total_jenis = len(items)
    total_stok = int(items["Stok"].sum()) if not items.empty else 0
    total_nilai = float((items["Stok"] * items["Harga"]).sum()) if not items.empty else 0
    stok_rendah = int((items["Stok"] <= items["Minimum Stok"]).sum()) if not items.empty else 0

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Jenis Barang", total_jenis)
    c2.metric("Total Stok", total_stok)
    c3.metric("Nilai Gudang", rupiah(total_nilai))
    c4.metric("Stok Rendah", stok_rendah)


def render_dashboard(items, suppliers, transactions, petugas):
    render_hero()
    render_stat_cards(items)

    st.write("")

    col_left, col_right = st.columns([1.25, 0.85], gap="large")

    with col_left:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="block-title">Grafik Kategori Barang</div>', unsafe_allow_html=True)

        if items.empty:
            st.info("Belum ada data barang.")
        else:
            cat_df = items.groupby("Kategori", as_index=False)["Stok"].sum()
            fig = px.bar(
                cat_df,
                x="Kategori",
                y="Stok",
                text="Stok",
                title=None,
            )
            fig.update_layout(
                height=340,
                margin=dict(l=10, r=10, t=10, b=10),
                xaxis_title="",
                yaxis_title="Stok",
                paper_bgcolor="white",
                plot_bgcolor="white",
            )
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

        st.write("")

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="block-title">Data Barang</div>', unsafe_allow_html=True)

        if items.empty:
            st.warning("Belum ada data barang.")
        else:
            show_df = items.copy()
            show_df["Status"] = show_df.apply(lambda x: status_stok(x["Stok"], x["Minimum Stok"]), axis=1)
            show_df["Nilai"] = show_df["Stok"] * show_df["Harga"]
            st.dataframe(
                show_df,
                use_container_width=True,
                hide_index=True
            )

        st.markdown("</div>", unsafe_allow_html=True)

    with col_right:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="block-title">Stok Rendah</div>', unsafe_allow_html=True)

        if items.empty:
            st.info("Belum ada barang.")
        else:
            low_stock = items[items["Stok"] <= items["Minimum Stok"]].copy()
            if low_stock.empty:
                st.success("Semua stok masih aman.")
            else:
                low_stock = low_stock[["Kode", "Nama Barang", "Stok", "Minimum Stok", "Lokasi Rak"]]
                st.dataframe(low_stock, use_container_width=True, hide_index=True)

        st.markdown("</div>", unsafe_allow_html=True)

        st.write("")

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="block-title">Transaksi Terbaru</div>', unsafe_allow_html=True)

        if transactions.empty:
            st.info("Belum ada transaksi.")
        else:
            latest = transactions.tail(8)[["Waktu", "Jenis", "Kode", "Nama Barang", "Jumlah"]]
            st.dataframe(latest, use_container_width=True, hide_index=True)

        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="block-title">Ringkasan Cepat</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    c1.info(f"Petugas aktif: **{petugas}**")
    c2.info(f"Supplier terdaftar: **{len(suppliers)}**")
    c3.info(f"Transaksi tercatat: **{len(transactions)}**")

    st.markdown("</div>", unsafe_allow_html=True)


def render_item_page(items):
    st.markdown("### 📋 Data Barang")

    tab1, tab2 = st.tabs(["Tambah / Update", "Daftar Barang"])

    with tab1:
        col1, col2 = st.columns([1.1, 0.9], gap="large")

        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="block-title">Form Barang</div>', unsafe_allow_html=True)

            existing_codes = items["Kode"].tolist() if not items.empty else []
            mode = st.radio("Mode", ["Tambah Baru", "Update Barang"], horizontal=True)

            with st.form("form_barang", clear_on_submit=False):
                if mode == "Update Barang" and existing_codes:
                    kode = st.selectbox("Kode Barang", existing_codes)
                    row = items[items["Kode"] == kode].iloc[0]
                    nama = st.text_input("Nama Barang", value=str(row["Nama Barang"]))
                    kategori = st.text_input("Kategori", value=str(row["Kategori"]))
                    lokasi = st.text_input("Lokasi Rak", value=str(row["Lokasi Rak"]))
                    stok = st.number_input("Stok", min_value=0, step=1, value=int(row["Stok"]))
                    minimum = st.number_input("Minimum Stok", min_value=0, step=1, value=int(row["Minimum Stok"]))
                    harga = st.number_input("Harga", min_value=0.0, step=1000.0, value=float(row["Harga"]))
                    deskripsi = st.text_area("Deskripsi", value=str(row["Deskripsi"]))
                else:
                    kode = st.text_input("Kode Barang")
                    nama = st.text_input("Nama Barang")
                    kategori = st.text_input("Kategori")
                    lokasi = st.text_input("Lokasi Rak")
                    stok = st.number_input("Stok", min_value=0, step=1, value=0)
                    minimum = st.number_input("Minimum Stok", min_value=0, step=1, value=5)
                    harga = st.number_input("Harga", min_value=0.0, step=1000.0, value=0.0)
                    deskripsi = st.text_area("Deskripsi")

                submit = st.form_submit_button("Simpan Barang")

            if submit:
                if not kode or not nama:
                    st.error("Kode dan nama barang wajib diisi.")
                else:
                    new_row = pd.DataFrame([{
                        "Kode": kode.strip().upper(),
                        "Nama Barang": nama.strip(),
                        "Kategori": kategori.strip(),
                        "Lokasi Rak": lokasi.strip(),
                        "Stok": int(stok),
                        "Minimum Stok": int(minimum),
                        "Harga": float(harga),
                        "Deskripsi": deskripsi.strip(),
                    }])

                    if mode == "Update Barang":
                        items = items[items["Kode"] != kode.strip().upper()]
                        items = pd.concat([items, new_row], ignore_index=True)
                        st.success("Barang berhasil diperbarui.")
                    else:
                        if kode.strip().upper() in items["Kode"].astype(str).tolist():
                            st.error("Kode barang sudah ada. Gunakan kode lain.")
                            st.stop()
                        items = pd.concat([items, new_row], ignore_index=True)
                        st.success("Barang berhasil ditambahkan.")

                    save_csv(items, ITEM_FILE)
                    st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="block-title">Hapus Barang</div>', unsafe_allow_html=True)

            if items.empty:
                st.info("Belum ada barang untuk dihapus.")
            else:
                kode_hapus = st.selectbox("Pilih barang", items["Kode"].tolist(), key="hapus_barang")
                if st.button("Hapus Barang"):
                    items = items[items["Kode"] != kode_hapus].copy()
                    save_csv(items, ITEM_FILE)
                    st.success("Barang berhasil dihapus.")
                    st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="block-title">Daftar Barang</div>', unsafe_allow_html=True)

        if items.empty:
            st.warning("Belum ada data barang.")
        else:
            q = st.text_input("Cari barang", placeholder="Ketik kode / nama / kategori...")
            view = items.copy()

            if q.strip():
                q2 = q.lower()
                view = view[
                    view["Kode"].astype(str).str.lower().str.contains(q2)
                    | view["Nama Barang"].astype(str).str.lower().str.contains(q2)
                    | view["Kategori"].astype(str).str.lower().str.contains(q2)
                ]

            view["Status"] = view.apply(lambda x: status_stok(x["Stok"], x["Minimum Stok"]), axis=1)
            view["Nilai"] = view["Stok"] * view["Harga"]

            st.dataframe(view, use_container_width=True, hide_index=True)

        st.markdown("</div>", unsafe_allow_html=True)


def render_supplier_page(suppliers):
    st.markdown("### 🚚 Supplier")

    col1, col2 = st.columns([1.0, 1.0], gap="large")

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="block-title">Tambah Supplier</div>', unsafe_allow_html=True)

        with st.form("form_supplier"):
            nama = st.text_input("Nama Supplier")
            telepon = st.text_input("Telepon")
            alamat = st.text_area("Alamat")
            submit = st.form_submit_button("Simpan Supplier")

        if submit:
            if not nama:
                st.error("Nama supplier wajib diisi.")
            else:
                new_id = next_id(suppliers, "SP")
                row = pd.DataFrame([{
                    "ID": new_id,
                    "Nama Supplier": nama.strip(),
                    "Telepon": telepon.strip(),
                    "Alamat": alamat.strip(),
                }])
                suppliers = pd.concat([suppliers, row], ignore_index=True)
                save_csv(suppliers, SUPPLIER_FILE)
                st.success("Supplier berhasil ditambahkan.")
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="block-title">Hapus Supplier</div>', unsafe_allow_html=True)

        if suppliers.empty:
            st.info("Belum ada supplier.")
        else:
            pilih = st.selectbox("Pilih supplier", suppliers["ID"].tolist(), key="hapus_supplier")
            if st.button("Hapus Supplier"):
                suppliers = suppliers[suppliers["ID"] != pilih].copy()
                save_csv(suppliers, SUPPLIER_FILE)
                st.success("Supplier berhasil dihapus.")
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="block-title">Daftar Supplier</div>', unsafe_allow_html=True)

    if suppliers.empty:
        st.warning("Belum ada data supplier.")
    else:
        st.dataframe(suppliers, use_container_width=True, hide_index=True)

    st.markdown("</div>", unsafe_allow_html=True)


def render_in_page(items, transactions, petugas):
    st.markdown("### 📥 Barang Masuk")

    if items.empty:
        st.warning("Belum ada barang. Tambahkan data barang terlebih dahulu.")
        return

    col1, col2 = st.columns([1.0, 1.0], gap="large")

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="block-title">Input Barang Masuk</div>', unsafe_allow_html=True)

        with st.form("form_masuk"):
            kode = st.selectbox("Pilih Barang", items["Kode"].tolist())
            qty = st.number_input("Jumlah Masuk", min_value=1, step=1, value=1)
            sumber = st.text_input("Sumber / Supplier")
            ket = st.text_area("Keterangan", value="Barang masuk ke gudang")
            submit = st.form_submit_button("Proses Masuk")

        if submit:
            idx = items[items["Kode"] == kode].index[0]
            items.loc[idx, "Stok"] = int(items.loc[idx, "Stok"]) + int(qty)
            save_csv(items, ITEM_FILE)

            nama = items.loc[idx, "Nama Barang"]
            transactions = add_transaction(
                transactions,
                "Masuk",
                kode,
                nama,
                qty,
                petugas,
                f"{ket} | Sumber: {sumber}"
            )

            st.success("Barang masuk berhasil disimpan.")
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="block-title">Stok Setelah Masuk</div>', unsafe_allow_html=True)
        view = items[["Kode", "Nama Barang", "Stok", "Minimum Stok", "Lokasi Rak"]].copy()
        st.dataframe(view, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)


def render_out_page(items, transactions, petugas):
    st.markdown("### 📤 Barang Keluar")

    if items.empty:
        st.warning("Belum ada barang. Tambahkan data barang terlebih dahulu.")
        return

    col1, col2 = st.columns([1.0, 1.0], gap="large")

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="block-title">Input Barang Keluar</div>', unsafe_allow_html=True)

        with st.form("form_keluar"):
            kode = st.selectbox("Pilih Barang", items["Kode"].tolist(), key="kode_keluar")
            qty = st.number_input("Jumlah Keluar", min_value=1, step=1, value=1)
            tujuan = st.text_input("Tujuan / Customer")
            ket = st.text_area("Keterangan", value="Barang keluar dari gudang")
            submit = st.form_submit_button("Proses Keluar")

        if submit:
            idx = items[items["Kode"] == kode].index[0]
            stok_sekarang = int(items.loc[idx, "Stok"])

            if stok_sekarang < int(qty):
                st.error(f"Stok tidak cukup. Stok tersedia: {stok_sekarang}")
            else:
                items.loc[idx, "Stok"] = stok_sekarang - int(qty)
                save_csv(items, ITEM_FILE)

                nama = items.loc[idx, "Nama Barang"]
                transactions = add_transaction(
                    transactions,
                    "Keluar",
                    kode,
                    nama,
                    qty,
                    petugas,
                    f"{ket} | Tujuan: {tujuan}"
                )

                st.success("Barang keluar berhasil disimpan.")
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="block-title">Daftar Stok Terkini</div>', unsafe_allow_html=True)
        view = items[["Kode", "Nama Barang", "Stok", "Minimum Stok", "Lokasi Rak"]].copy()
        st.dataframe(view, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)


def export_excel(items, suppliers, transactions):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        items.to_excel(writer, sheet_name="Barang", index=False)
        suppliers.to_excel(writer, sheet_name="Supplier", index=False)
        transactions.to_excel(writer, sheet_name="Transaksi", index=False)
    output.seek(0)
    return output


def render_report_page(items, suppliers, transactions):
    st.markdown("### 📊 Laporan Gudang")

    col1, col2 = st.columns([1.0, 1.0], gap="large")

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="block-title">Ringkasan Inventaris</div>', unsafe_allow_html=True)

        total_nilai = float((items["Stok"] * items["Harga"]).sum()) if not items.empty else 0
        total_jenis = len(items)
        total_stok = int(items["Stok"].sum()) if not items.empty else 0
        stok_rendah = int((items["Stok"] <= items["Minimum Stok"]).sum()) if not items.empty else 0

        a, b = st.columns(2)
        a.metric("Jenis Barang", total_jenis)
        b.metric("Total Stok", total_stok)
        c, d = st.columns(2)
        c.metric("Nilai Gudang", rupiah(total_nilai))
        d.metric("Stok Rendah", stok_rendah)

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="block-title">Download Laporan</div>', unsafe_allow_html=True)

        csv_barang = items.to_csv(index=False).encode("utf-8")
        csv_transaksi = transactions.to_csv(index=False).encode("utf-8")

        excel_file = export_excel(items, suppliers, transactions)

        st.download_button(
            "Download Barang CSV",
            data=csv_barang,
            file_name="barang.csv",
            mime="text/csv"
        )
        st.download_button(
            "Download Transaksi CSV",
            data=csv_transaksi,
            file_name="transaksi.csv",
            mime="text/csv"
        )
        st.download_button(
            "Download Excel Lengkap",
            data=excel_file.getvalue(),
            file_name="laporan_gudang.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    tab1, tab2 = st.tabs(["Tabel Barang", "Riwayat Transaksi"])

    with tab1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        if items.empty:
            st.warning("Belum ada barang.")
        else:
            df = items.copy()
            df["Status"] = df.apply(lambda x: status_stok(x["Stok"], x["Minimum Stok"]), axis=1)
            df["Nilai"] = df["Stok"] * df["Harga"]
            st.dataframe(df, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        if transactions.empty:
            st.warning("Belum ada transaksi.")
        else:
            t = transactions.copy()
            t["Waktu"] = pd.to_datetime(t["Waktu"], errors="coerce")
            st.dataframe(t, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)


def main():
    inject_css()

    items, suppliers, transactions = load_all_data()

    st.sidebar.title("📦 Warehouse Control")
    st.sidebar.caption("Tampilan modern gudang")

    petugas = st.sidebar.text_input("Nama Petugas", value="Admin")
    menu = st.sidebar.radio(
        "Menu",
        ["Dashboard", "Data Barang", "Barang Masuk", "Barang Keluar", "Supplier", "Laporan"]
    )

    st.sidebar.divider()
    st.sidebar.caption(f"Login aktif: {petugas}")

    if menu == "Dashboard":
        render_dashboard(items, suppliers, transactions, petugas)
    elif menu == "Data Barang":
        render_item_page(items)
    elif menu == "Barang Masuk":
        render_in_page(items, transactions, petugas)
    elif menu == "Barang Keluar":
        render_out_page(items, transactions, petugas)
    elif menu == "Supplier":
        render_supplier_page(suppliers)
    elif menu == "Laporan":
        render_report_page(items, suppliers, transactions)


if __name__ == "__main__":
    main()
