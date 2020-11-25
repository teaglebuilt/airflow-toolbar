from airflow.plugins_manager import AirflowPlugin
from src.dashboard import dashboard
from flask import Blueprint


blue_print = Blueprint(
    "toolbar",
    __name__,
    template_folder='templates',
    static_folder='static'
)


class AirflowToolbar(AirflowPlugin):
    """Class to register plugin to airflow"""
    name = "Airflow Toolbar"
    admin_views = [dashboard]
    flask_blueprints = [blue_print]