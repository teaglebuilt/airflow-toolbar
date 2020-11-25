from airflow.plugins_manager import AirflowPlugin
from flask_admin import BaseView, expose



class DashboardView(BaseView):
    """View for airflow toolbar"""
    @expose("/")
    def index(self):
        data = [{'column_a': 'Content',
                 'column_b': '123',
                 'column_c': 'Test'}]
        return self.render(
            "base.html", 
            data=data
        )
            
dashboard = DashboardView(category="Toolbar", name="dashboard")