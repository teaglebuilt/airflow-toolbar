from pathlib import Path
from unittest.mock import patch, MagicMock
from airflow.www import app as application
from flask import config
import pytest


def test_dashboard_view(mock_airflow_db):
    TEST_DB = "test.db"
    BASE_DIR = Path(__file__).resolve().parent.parent
    app = application.create_app(testing=True)
    app.config['WTF_CSRF_ENABLED'] = False
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{BASE_DIR.joinpath(TEST_DB)}"
    client = app.test_client()
    resp = client.get('http://localhost:8080/admin/dashboardview/')
    assert resp.status_code == 200
    
