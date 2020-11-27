from setuptools import setup, find_packages

setup(
    name="airflow-toolbar",
    description="Airflow Debugging Toolbar UI",
    packages=find_packages(
        exclude=('tests*')
    ),
    entry_points = {
        'airflow.plugins': [
            'my_plugin = src.plugin:AirflowToolbar'
        ]
    },
    extras_require={}
)