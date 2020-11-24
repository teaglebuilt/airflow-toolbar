import os
from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint
from flask_admin import BaseView, expose
from flask_admin.base import MenuLink


class DashboardView(BaseView):
    """View for airflow toolbar"""
    @expose("/")
    def index(self):
        data = [{'column_a': 'Content',
                 'column_b': '123',
                 'column_c': 'Test'}]
        return self.render("base.html", data=data)


dashboard = DashboardView(category="Toolbar", name="dashboard")


blue_print_ = Blueprint("toolbar",
                        __name__,
                        template_folder='templates',
                        static_folder='static')


class AirflowToolbar(AirflowPlugin):
    """Class to register plugin to airflow"""
    name = "Airflow Toolbar"
    admin_views = [dashboard]
    flask_blueprints = [blue_print_]