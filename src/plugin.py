from airflow.plugins_manager import AirflowPlugin



class AirflowToolbar(AirflowPlugin):
    """Class to register plugin to airflow"""
    name = "Airflow Toolbar"
