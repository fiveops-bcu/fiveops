import pytest

from app import create_app

TEST_CONFIG = {"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite://"}


@pytest.fixture
def client():
    return create_app(TEST_CONFIG).test_client()


@pytest.fixture
def customer_id(client):
    body = {"name": "Ada", "email": "ada@example.com"}
    return client.post("/customers", json=body).get_json()["id"]
