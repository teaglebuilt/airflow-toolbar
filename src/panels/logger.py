import logging
import threading
from airflow import LoggingMixin


class ThreadTrackingHandler(logging.Handler):
    """Logging Handler"""
    def __init__(self):
        logging.Handler.__init__(self)
        self.records = {}

    def emit(self, record):
        return self.get_records().append(record)

    def get_records(self, thread=None):
        if thread is None:
            thread = threading.currentThread()
        if thread not in self.records:
            self.records[thread] = []
        return self.records[thread]


class AirflowLogHandler(ThreadTrackingHandler, LoggingMixin):
    pass