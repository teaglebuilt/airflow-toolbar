import logging
from airflow import logging_config


gunicorn_logger = logging.getLogger('gunicorn.error')
