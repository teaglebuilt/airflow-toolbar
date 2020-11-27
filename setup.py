from setuptools import setup

setup(
    name="airflow-toolbar",
    description="Airflow Debugging Toolbar UI",
    entry_points = {
        'airflow.plugins': [
            'my_plugin = src.plugin:AirflowToolbar'
        ]
    },
    extras_require={}
)