import streamlit as st
import pandas as pd


class AkunView:

    def __init__(self, controller):
        self.controller = controller

    def render(self):

        if st.session_state.role != "Admin":

            st.error(
                "Hanya Admin Yang Dapat Mengakses Menu Ini"
            )

            return

        st.title("Manajemen Akun")

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "Daftar Akun",
                "Tambah Akun",
                "Hapus Akun",
                "Riwayat Login"
            ]
        )

        with tab1:

            akun = self.controller.get_all_akun()

            st.dataframe(
                pd.DataFrame(akun),
                use_container_width=True
            )

        with tab2:
            with st.form("akun", clear_on_submit=True):
                username = st.text_input(
                    "Username"
                )

                password = st.text_input(
                    "Password"
                )

                role = st.selectbox(
                    "Role",
                    [
                        "Admin",
                        "User"
                    ]
                )

                if st.form_submit_button(
                    "Tambah Akun"
                ):

                    status, pesan = self.controller.tambah_akun(
                        username,
                        password,
                        role
                    )

                    if status:
                        st.success(pesan)
                    else:
                        st.error(pesan)
            
        with tab3:

            username_list = [
            item["Username"]
            for item in self.controller.get_all_akun()
        ]

            hapus_akun = st.selectbox(
            "Pilih Akun",
            ["-"] + username_list
        )

            if st.button("Hapus Akun"):

                if hapus_akun == "-":
                    st.error("Pilih akun terlebih dahulu")

                else:

                    status, pesan = (
                        self.controller.hapus_akun(
                            hapus_akun
                        )
                    )

                    if status:
                        st.success(pesan)
                        st.rerun()

                    else:
                        st.error(pesan)
        
        with tab4:
            riwayat_list = self.controller.get_all_riwayat()
            
            st.dataframe(
                pd.DataFrame(riwayat_list[::-1]), use_container_width=True)