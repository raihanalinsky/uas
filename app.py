import streamlit as st

# ====================
# import controller
# ====================
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

# ================================
# title website
# ================================
st.set_page_config(
    page_title="Warehouse Management System", page_icon="📦", layout="wide"
)

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* BACKGROUND */

.stApp{

    background:
    linear-gradient(
        rgba(15,23,42,0.94),
        rgba(15,23,42,0.94)
    ),
    url("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d");

    background-size:cover;
    background-attachment:fixed;
}

/* SIDEBAR */

section[data-testid="stSidebar"]{

    background:
    rgba(15,23,42,.95);

    backdrop-filter:blur(20px);

    border-right:
    1px solid rgba(255,255,255,.1);
}

section[data-testid="stSidebar"] *{

    color:#F8FAFC !important;
}

/* HEADER */

.hero-card{

    background:
    rgba(15,23,42,.85);

    backdrop-filter:blur(20px);

    padding:35px;

    border-radius:24px;

    border:
    1px solid rgba(255,255,255,.08);

    box-shadow:
    0 8px 32px rgba(0,0,0,.35);

    margin-bottom:25px;
}

.hero-title{

    color:#F8FAFC;

    font-size:40px;

    font-weight:700;

    margin-bottom:10px;
}

.hero-sub{

    color:#CBD5E1;

    font-size:17px;
}

/* METRIC */

div[data-testid="metric-container"]{

    background:
    rgba(15,23,42,.82);

    backdrop-filter:blur(15px);

    border-radius:22px;

    padding:25px;

    border:
    1px solid rgba(255,255,255,.08);

    box-shadow:
    0 8px 25px rgba(0,0,0,.25);
}

div[data-testid="metric-container"] label{

    color:#CBD5E1 !important;
}

div[data-testid="metric-container"] [data-testid="stMetricValue"]{

    color:#22C55E !important;

    font-size:32px;
}

/* TABLE */

[data-testid="stDataFrame"]{

    background:
    rgba(15,23,42,.85);

    border-radius:22px;

    padding:15px;

    border:
    1px solid rgba(255,255,255,.08);

    box-shadow:
    0 8px 25px rgba(0,0,0,.25);
}

/* INPUT */

.stTextInput input,
.stNumberInput input{

    background:#1E293B !important;

    color:white !important;

    border:1px solid #334155 !important;

    border-radius:12px !important;
}

.stSelectbox div[data-baseweb="select"]{

    background:#1E293B !important;

    color:white !important;

    border-radius:12px !important;
}

/* BUTTON */

.stButton button{

    background:
    linear-gradient(
        135deg,
        #22C55E,
        #16A34A
    ) !important;

    color:white !important;

    border:none !important;

    border-radius:14px !important;

    height:48px;

    font-weight:600;
}

.stButton button:hover{

    transform:translateY(-2px);

    box-shadow:
    0 0 20px rgba(34,197,94,.5);
}

/* TAB */

.stTabs [role="tab"]{

    background:
    rgba(15,23,42,.75);

    color:white;

    border-radius:12px;
}

.stTabs [aria-selected="true"]{
    color:white !important;
}

/* TEXT */

h1,h2,h3,h4,h5,h6{

    color:#F8FAFC !important;
}

p,span,label{

    color:#CBD5E1 !important;
}

/* EXPANDER */

.streamlit-expanderHeader{

    color:white !important;
}

/* ALERT */

.stSuccess{

    border-left:
    6px solid #22C55E;
}

.stWarning{

    border-left:
    6px solid #F59E0B;
}

.stError{

    border-left:
    6px solid #EF4444;
}

</style>
""",
    unsafe_allow_html=True,
)

# ==================================================
# untuk menyimpan session login, username, dan role
# ==================================================

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
    LoginView(auth_controller).render()

    st.stop()


# ==========================
# Sidebar
# ==========================

st.sidebar.title("Warehouse Troops")

menu = st.sidebar.selectbox(
    "Menu", ["Dashboard", "Barang", "Supplier", "Laporan", "Akun"]
)

st.sidebar.write(f"Login sebagai : {st.session_state.username}")

if st.sidebar.button("Logout"):
    auth_controller.logout(st.session_state["username"])

    st.session_state.login = False
    st.session_state.username = None
    st.session_state.role = None

    st.rerun()


# ==================================
# ketika memilih pages di sidebar
# ==================================

if menu == "Dashboard":
    DashboardView(dashboard_controller, laporan_controller).render()

elif menu == "Barang":
    BarangView(barang_controller, supplier_controller).render()

elif menu == "Supplier":
    SupplierView(supplier_controller).render()

elif menu == "Laporan":
    LaporanView(laporan_controller).render()

elif menu == "Akun":
    AkunView(akun_controller).render()
