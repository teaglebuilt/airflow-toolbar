from setuptools import setup, find_packages


def get_extra_requires(path, all=True):
    """https://hanxiao.io/2019/11/07/A-Better-Practice-for-Managing-extras-require-Dependencies-in-Python/"""
    pass


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
    extras_require=get_extra_requires('requirements/extra.txt')
)