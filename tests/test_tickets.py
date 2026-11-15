import pytest


def new_ticket(client, customer_id, subject="Login broken"):
    body = {"customer_id": customer_id, "subject": subject}
    return client.post("/tickets", json=body)


def test_create_customer(client):
    body = {"name": "Sam", "email": "SAM@Example.com"}
    res = client.post("/customers", json=body)
    assert res.status_code == 201
    assert res.get_json()["email"] == "sam@example.com"


@pytest.mark.parametrize("body", [
    {}, {"name": "Sam"}, {"name": "Sam", "email": "not-an-email"}])
def test_customer_needs_name_and_valid_email(client, body):
    assert client.post("/customers", json=body).status_code == 400


def test_duplicate_email_rejected(client, customer_id):
    body = {"name": "Ada 2", "email": "ada@example.com"}
    assert client.post("/customers", json=body).status_code == 409


def test_create_and_list_ticket(client, customer_id):
    res = new_ticket(client, customer_id)
    assert res.status_code == 201
    assert res.get_json()["status"] == "open"
    listed = client.get("/tickets?status=open").get_json()
    assert [t["subject"] for t in listed] == ["Login broken"]


def test_ticket_for_unknown_customer(client):
    assert new_ticket(client, 999).status_code == 404


def test_ticket_needs_subject(client, customer_id):
    assert new_ticket(client, customer_id, "  ").status_code == 400


def test_update_status(client, customer_id):
    tid = new_ticket(client, customer_id).get_json()["id"]
    closed = client.patch(f"/tickets/{tid}", json={"status": "closed"})
    assert closed.get_json()["status"] == "closed"
    bad = client.patch(f"/tickets/{tid}", json={"status": "lost"})
    assert bad.status_code == 400
    missing = client.patch("/tickets/999", json={"status": "closed"})
    assert missing.status_code == 404
