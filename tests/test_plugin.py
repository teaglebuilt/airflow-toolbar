import inspect
import logging
import unittest

from airflow.plugins_manager import AirflowPlugin, is_valid_plugin

import src


def isplugin(x):
    if inspect.isclass(x):
        return (
            issubclass(x, AirflowPlugin) and x.__name__ != "AirflowPlugin"
        )
    return False

def islocalmodule(x):
    if inspect.ismodule(x):
        return src.__name__ in x.__name__
    return False


def get_all_plugins(module, plugins=[]):  # pylint: disable=redefined-outer-name
    inspection = inspect.getmembers(module, isplugin)
    if inspection:
        plugins.extend(inspection)
    modules = [x[1] for x in inspect.getmembers(module, islocalmodule)]

    while modules:
        for module in modules:  # pylint: disable=redefined-argument-from-local
            get_all_plugins(module, plugins)
            modules.remove(module)

    return plugins


class TestPlugins(unittest.TestCase):
    """
    Test custom plugin to ensure it integrates with Airflow
    """
    @classmethod
    def setUpClass(cls):
        cls.plugins = get_all_plugins(module=src)

    def test_plugin_validity(self):
        for name, plugin in self.plugins:
            logging.info("Validating %s", name)
            self.assertTrue(is_valid_plugin(plugin, ['AirflowToolbar']))