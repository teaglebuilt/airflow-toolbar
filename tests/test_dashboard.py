from tests.conftest import mock_airflow_db
from airflow.www import app as application
from flask import config
import pytest


with mock_airflow_db() as db:
    def test_dashboard_view():
        app = application.create_app(testing=True)
        app.config["SQLALCHEMY_DATABASE_URI"] = db.sql_alchemy_conn
        client = app.test_client()
        resp = client.get('http://localhost:8080/admin/dashboardview/')
        assert resp.status_code == 200
    