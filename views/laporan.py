import streamlit as st
import pandas as pd


class LaporanView:

    def __init__(self, controller):
        self.controller = controller

    def render(self):

        st.title("📈 Laporan")

        transaksi = self.controller.get_laporan_transaksi()

        df = pd.DataFrame(transaksi)

        st.dataframe(
            df,
            use_container_width=True
        )

        st.metric(
            "Total Barang Masuk",
            self.controller.total_barang_masuk()
        )

        st.metric(
            "Total Barang Keluar",
            self.controller.total_barang_keluar()
        )

        csv = df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "Download CSV",
            csv,
            "laporan.csv",
            "text/csv"
        )