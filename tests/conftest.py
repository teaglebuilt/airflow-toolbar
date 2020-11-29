import os
from unittest.mock import patch
from typing import ContextManager
import pytest


@pytest.fixture
def mock_env() -> ContextManager[dict]:
    with patch.dict('os.environ', {
        "AIRFLOW_HOME": os.path.abspath(os.curdir)
    }) as mock_env:
        yield mock_env