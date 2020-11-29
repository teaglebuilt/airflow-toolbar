from airflow.www import app as application
from werkzeug.routing import Rule
from werkzeug.test import create_environ
from werkzeug.wrappers import Response
from flask import config


def test_dashboard_view(mock_env):
    app = application.create_app(testing=True)
    app.config['WTF_CSRF_ENABLED'] = False
    client = app.test_client()
    resp = client.get('http://localhost:8080/admin/dashboardview/')
    assert resp.status_code == 200
    