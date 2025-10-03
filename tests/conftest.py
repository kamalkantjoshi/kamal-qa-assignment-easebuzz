import pytest
import requests


@pytest.fixture(scope="session")
def api_client():
    # Fixture to provide a session for making API requests.
    with requests.Session() as session:
        yield session