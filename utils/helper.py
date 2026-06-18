import streamlit as st

#mengecek apakah role admin atau bukan
def is_admin():
    if st.session_state.get("role") == "Admin":
        return True
    st.error("Hanya Admin yang boleh mengakses fitur ini!")
    return False

#untuk mendapatkan kode di awal dengan memisahkan -
def get_barang_kode(selected):
    if selected == "-":
        return None
    
    return selected.split("-")[0]