import streamlit as st


class LoginView:

    def __init__(self, controller):
        self.controller = controller

    def render(self):

        st.title("Login")

        username = st.text_input(
            "Username"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            status, user = self.controller.login(
                username,
                password
            )

            if status:

                st.session_state.login = True
                st.session_state.username = user["Username"]
                st.session_state.role = user["Role"]

                st.rerun()

            else:

                st.error(
                    "Username atau Password Salah"
                )