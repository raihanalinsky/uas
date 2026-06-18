import streamlit as st

from controllers.auth_controller import AuthController
from controllers.barang_controller import BarangController
from controllers.supplier_controller import SupplierController
from controllers.akun_controller import AkunController
from controllers.dashboard_controller import DashboardController
from controllers.laporan_controller import LaporanController

from views.login import LoginView
from views.dashboard import DashboardView
from views.barang import BarangView
from views.supplier import SupplierView
from views.laporan import LaporanView
from views.akun import AkunView

st.set_page_config(
    page_title="Warehouse Management System",
    page_icon="📦",
    layout="wide"
)

# ==========================
# Session
# ==========================

if "login" not in st.session_state:
    st.session_state.login = False

if "username" not in st.session_state:
    st.session_state.username = None

if "role" not in st.session_state:
    st.session_state.role = None


# ==========================
# Controller
# ==========================

auth_controller = AuthController()
barang_controller = BarangController()
supplier_controller = SupplierController()
akun_controller = AkunController()
dashboard_controller = DashboardController()
laporan_controller = LaporanController()


# ==========================
# Login
# ==========================

if not st.session_state.login:

    LoginView(
        auth_controller
    ).render()

    st.stop()


# ==========================
# Sidebar
# ==========================

st.sidebar.title("Warehouse Troops")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Dashboard",
        "Barang",
        "Supplier",
        "Laporan",
        "Akun"
    ]
)

st.sidebar.write(
    f"Login sebagai : {st.session_state.username}"
)

if st.sidebar.button("Logout"):
    
    auth_controller.logout(st.session_state["username"])

    st.session_state.login = False
    st.session_state.username = None
    st.session_state.role = None

    st.rerun()


# ==========================
# Routing
# ==========================

if menu == "Dashboard":

    DashboardView(
        dashboard_controller
    ).render()

elif menu == "Barang":

    BarangView(
        barang_controller,
        supplier_controller
    ).render()

elif menu == "Supplier":

    SupplierView(
        supplier_controller
    ).render()

elif menu == "Laporan":

    LaporanView(
        laporan_controller
    ).render()

elif menu == "Akun":

    AkunView(
        akun_controller
    ).render()