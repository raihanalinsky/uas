import streamlit as st


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