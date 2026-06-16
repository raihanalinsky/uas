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

        tab1, tab2 = st.tabs(
            [
                "Daftar Akun",
                "Tambah Akun"
            ]
        )

        with tab1:

            akun = self.controller.get_all_akun()

            st.dataframe(
                pd.DataFrame(akun),
                use_container_width=True
            )

        with tab2:

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

            if st.button(
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