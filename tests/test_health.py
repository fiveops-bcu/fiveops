def test_health_returns_ok(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}


def test_version_defaults_to_dev(client):
    assert client.get("/version").get_json() == {"version": "dev"}


def test_health_reports_database_down(client, monkeypatch):
    from app import db

    def broken(*args, **kwargs):
        raise RuntimeError("db gone")

    monkeypatch.setattr(db.session, "execute", broken)
    res = client.get("/health")
    assert res.status_code == 503
    assert res.get_json()["database"] == "down"
