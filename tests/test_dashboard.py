from airflow import settings
from airflow.www import app as application
from airflow.settings import Session
from flask import config
import jinja2
import pytest


def test_dashboard_view(mock_env):
    settings.configure_orm()
    app = application.create_app(testing=True)
    app.config['WTF_CSRF_ENABLED'] = False
    app.jinja_env.undefined = jinja2.StrictUndefined
    client = app.test_client()
    resp = client.get('http://localhost:8080/admin/dashboardview/')
    assert resp.status_code == 200
    