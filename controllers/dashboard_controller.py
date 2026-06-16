from services.dashboard_service import DashboardService


class DashboardController:

    def __init__(self):

        self.service = DashboardService()

    def get_dashboard_data(self):

        return self.service.get_dashboard_data()