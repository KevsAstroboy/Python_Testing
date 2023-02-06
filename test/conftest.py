import pytest
from server import app
import json


@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client
