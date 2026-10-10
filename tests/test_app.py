import os
os.environ.setdefault("FLASK_SECRET", "test-secret-for-ci-only")

import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_login_page_loads(client):
    response = client.get("/login")
    assert response.status_code == 200


def test_dashboard_redirects_when_not_logged_in(client):
    response = client.get("/dashboard")
    assert response.status_code == 302