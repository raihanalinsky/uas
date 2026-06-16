import streamlit as st
import plotly.express as px
import pandas as pd


class DashboardView:

    def __init__(self, controller):
        self.controller = controller

    def render(self):

        st.title("Dashboard Gudang")

        data = self.controller.get_dashboard_data()

        c1, c2, c3, c4, c5 = st.columns(5)

        c1.metric(
            "Jenis Barang",
            data["total_barang"]
        )

        c2.metric(
            "Total Stok",
            data["total_stok"]
        )

        c3.metric(
            "Nilai Inventaris",
            f"Rp {data['total_nilai']:,.0f}"
        )

        c4.metric(
            "Stok Menipis",
            data["stok_menipis"]
        )

        c5.metric(
            "Supplier",
            data["total_supplier"]
        )
        
        bm = self.controller.get_barang_masuk()
        bk = self.controller.get_barang_keluar()

        grafik = {
            "Jenis": [
                "Barang Masuk",
                "Barang Keluar"
            ],
            "Jumlah": [
                bm,
                bk
            ]
        }

        df = pd.DataFrame(grafik)

        fig_bar = px.bar(
            df,
            x="Jenis",
            y="Jumlah",
            color="Jenis",
            title="Perbandingan Barang Masuk dan Keluar"
        )

        st.plotly_chart(
            fig_bar,
            use_container_width=True
        )