import streamlit as st
import plotly.express as px
import pandas as pd


class DashboardView:
    def __init__(self, dashboard_controller, laporan_controller):
        self.dashboard_controller = dashboard_controller
        self.laporan_controller = laporan_controller

    def render(self):
        st.markdown(
            """
<div class="hero-card">

<div class="hero-title">
📦 Warehouse Management System
</div>

<div class="hero-sub">
Kelola stok barang, supplier,
barang masuk, barang keluar,
dan laporan inventaris secara real-time.
</div>

</div>
""",
            unsafe_allow_html=True,
        )
        data = self.dashboard_controller.get_dashboard_data()

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("📦 Jenis Barang", data["total_barang"])

        with c2:
            st.metric("📚 Total Stok", data["total_stok"])

        with c3:
            st.metric("⚠️ Stok Menipis", data["stok_menipis"])

        with c4:
            st.metric("🚚 Supplier", data["total_supplier"])

        # mengambil data barang masuk dan keluar dari service dengan dashboard_controller sebagai jembatannya
        barang_masuk = self.dashboard_controller.get_barang_masuk()
        barang_keluar = self.dashboard_controller.get_barang_keluar()

        # membuat data dict untuk jenis dan jumlah barang yang masuk dan keluar
        grafik = {
            "Jenis": ["Barang Masuk", "Barang Keluar"],
            "Jumlah": [barang_masuk, barang_keluar],
        }

        df = pd.DataFrame(grafik)

        # membuat grafik barang masuk dan keluar
        fig_bar = px.bar(
            df,
            x="Jenis",
            y="Jumlah",
            color="Jenis",
            text_auto=True,
            title="📦 Perbandingan Barang Masuk dan Keluar",
        )

        st.plotly_chart(fig_bar, use_container_width=True)

        st.divider()

        # membuat line grafik barang masuk dan keluar perbulan
        laporan_perbulan = self.laporan_controller.get_all_laporan_bulanan()

        fig = px.line(
            laporan_perbulan,
            x="Bulan",
            y=["Masuk", "Keluar"],
            markers=True,
            title="Trend barang masuk dan keluar per bulan",
        )

        st.plotly_chart(fig, use_container_width=True)

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(15,23,42,.8)",
            font=dict(color="#F8FAFC"),
            title_font_size=24,
            legend_font_color="#F8FAFC",
        )
