import pytest
import sys
import os
from pages_tests.data_api_import import SendApi
from utils.db_connect import db_conn, close_conn


@pytest.fixture(scope="session", autouse=True)
def endpoint_setup():
    tests_path = os.path.join(os.path.dirname(__file__), 'tests')
    if tests_path not in sys.path:
        sys.path.insert(0, tests_path)


@pytest.fixture
def info_api():
    return SendApi("test")


@pytest.fixture
def token_authorization():
    api = SendApi("test")
    return api.invoke_token_api()


@pytest.fixture
def db_connec():
    connection = db_conn()
    yield connection
    close_conn(connection)
