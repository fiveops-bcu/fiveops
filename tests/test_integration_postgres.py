import os
import uuid

import pytest

from app import create_app

URL = os.environ.get("TEST_DATABASE_URL")
pytestmark = pytest.mark.skipif(
    not URL, reason="needs PostgreSQL (runs in Jenkins)")


def test_ticket_round_trip_on_postgres():
    config = {"TESTING": True, "SQLALCHEMY_DATABASE_URI": URL}
    client = create_app(config).test_client()
    email = f"{uuid.uuid4().hex[:8]}@example.com"
    customer = {"name": "Int", "email": email}
    cid = client.post("/customers", json=customer).get_json()["id"]
    ticket = {"customer_id": cid, "subject": "DB test"}
    tid = client.post("/tickets", json=ticket).get_json()["id"]
    res = client.patch(f"/tickets/{tid}", json={"status": "closed"})
    assert res.status_code == 200
