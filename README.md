Sistem Manajemen Gudang (Warehause Troops)

Deskripsi Proyek

Sistem Manajemen Gudang merupakan aplikasi berbasis Python yang digunakan untuk membantu proses pengelolaan data barang pada gudang. Sistem ini dibangun menggunakan framework Streamlit dengan menerapkan arsitektur MVC (Model-View-Controller) sehingga kode lebih terstruktur, mudah dikembangkan, dan mudah dipelihara.

Aplikasi ini mendukung pengelolaan data barang, supplier, transaksi barang masuk, transaksi barang keluar, serta laporan stok secara real-time.

---

## Fitur Utama

### 1. Manajemen Barang
- Menambah data barang
- Edit data barang
- Menghapus data barang
- Mencari data barang
- Melihat daftar seluruh barang

### 2. Manajemen Supplier
- Menambah supplier
- Mengubah data supplier
- Menghapus supplier
- Melihat daftar supplier

### 3. Barang Masuk
- Mencatat transaksi barang masuk
- Menambah stok secara otomatis
- Menyimpan riwayat transaksi

### 4. Barang Keluar
- Mencatat transaksi barang keluar
- Mengurangi stok secara otomatis
- Validasi stok sebelum transaksi

### 5. Laporan
- Laporan stok barang
- Riwayat barang masuk
- Riwayat barang keluar
- Statistik transaksi

### 6. Sistem Login
- Login pengguna
- Logout pengguna
- Manajemen session

---

## Teknologi yang Digunakan
- Python
- Streamlit
- Pandas
- CSV
- MVC (Struktur Program)
- Linked List

## Struktru Folder
project_gudang/
app.py
-controllers/
  -akun_controller.py
  -auth_controller.py
  -barang_controller.py
  -dashboard_controller.py
  -supplier_controller.py
  -laporan_controller.py

-models/
  -akun_model.py
  -barang_model.py
  -linked_list.py
  -node.py
  -riwayat_login.py
  -supplier_model.py
  -transaksi_model.py

-services/
  -akun_service.py
  -auth_service.py
  -barang_service.py
  -dashboard_service.py
  -supplier_service.py
  -laporan_service.py
  
-views/
  -login.py
  -dashboard.py
  -barang.py
  -supplier.py
  -akun.py
  -laporan.py

-utils/
  -helper.py
  -path_helper.py

-database/
  -akun.csv
  -barang.csv
  -riwayat_login.csv
  -supplier.csv
  -transaksi.csv
-README.md
-requirements.txt


---

## Arsitektur MVC

### Model
Berfungsi mengelola data dan interaksi dengan penyimpanan data.

Contoh:
- BarangModel
- SupplierModel
- UserModel

### View
Berfungsi menampilkan antarmuka kepada pengguna menggunakan Streamlit.

Contoh:
- LoginView
- DashboardView
- BarangView

### Controller
Berfungsi sebagai penghubung antara View dan Service.

Contoh:
- BarangController
- AuthController

### Service
Berisi logika bisnis aplikasi.

Contoh:
- Validasi login
- Perhitungan stok
- Validasi transaksi

### Utils
menyimpan fungsi-fungsi bantuan (helper) yang dapat digunakan oleh berbagai bagian sistem.

Contoh:
- Validasi input pengguna.
- Format tanggal dan waktu.
- Pengelolaan session login pengguna.
  
---

## Implementasi Linked List

Linked List digunakan untuk:

- Menyimpan daftar barang
- Menampilkan data secara berurutan
- Operasi insert dan delete yang lebih efisien


##
Muhamad Raihan Alinsky & Khoirul Al Zuhri
