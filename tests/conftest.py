import os
import tempfile
import contextlib
from typing import ContextManager
from airflow import settings
from airflow.utils.db import initdb
from tests.utils.db import AirflowDB
import pytest


@contextlib.contextmanager
def mock_env(**environ) -> ContextManager[dict]:
    old_environ = dict(os.environ)
    os.environ.update(environ)
    try:
        yield
    finally:
        os.environ.clear()
        os.environ.update(old_environ)


@contextlib.contextmanager
def mock_airflow_db() -> ContextManager[AirflowDB]:
    with tempfile.TemporaryDirectory() as temp_dir:
        test_db_path = os.path.join(temp_dir, 'airflow.db')
        sql_alchemy_conn = f'sqlite:///{test_db_path}'
        with mock_env(
            AIRFLOW__CORE__SQL_ALCHEMY_CONN=f'sqlite:///{test_db_path}',
            AIRFLOW_HOME=os.path.abspath(os.curdir),
            PYTHONPATH=os.path.abspath(os.curdir)
            ):
            settings.configure_vars()
            settings.configure_orm()
            assert repr(settings.engine.url) == sql_alchemy_conn
            initdb()
            yield AirflowDB(sql_alchemy_conn=sql_alchemy_conn)
    settings.configure_vars()
    settings.configure_orm()
