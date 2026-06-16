from services.dashboard_service import DashboardService
from services.laporan_service import LaporanService


class DashboardController:

    def __init__(self):

        self.dash_service = DashboardService()
        self.laporan_servie = LaporanService()

    def get_dashboard_data(self):
        return self.dash_service.get_dashboard_data()
    
    def get_barang_masuk(self):
        return self.laporan_servie.total_barang_masuk()
        
    def get_barang_keluar(self):
        return self.laporan_servie.total_barang_keluar()
        