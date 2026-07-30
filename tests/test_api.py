"""
test_api.py
----------------------------------------
API Tests for Phishing Detection Flask App
Run:
    pytest tests/test_api.py
"""

import pytest

from app.app import app


# -----------------------------------------
# Create Test Client
# -----------------------------------------

@pytest.fixture
def client():

    app.config["TESTING"] = True

    with app.test_client() as client:

        yield client


# -----------------------------------------
# Test Home Page
# -----------------------------------------

def test_home_page(client):

    response = client.get("/")

    assert response.status_code == 200


# -----------------------------------------
# Test Health Endpoint
# -----------------------------------------

def test_health_endpoint(client):

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "running"

    assert data["application"] == "Phishing URL Detection"


# -----------------------------------------
# Test Valid Prediction
# -----------------------------------------

def test_predict_valid_url(client):

    response = client.post(

        "/predict",

        data={

            "url": "https://www.google.com"

        }

    )

    assert response.status_code == 200


# -----------------------------------------
# Test Empty URL
# -----------------------------------------

def test_predict_empty_url(client):

    response = client.post(

        "/predict",

        data={

            "url": ""

        }

    )

    assert response.status_code == 200

    assert b"Please enter a URL." in response.data


# -----------------------------------------
# Test Long URL
# -----------------------------------------

def test_predict_long_url(client):

    long_url = "https://example.com/" + "a" * 500

    response = client.post(

        "/predict",

        data={

            "url": long_url

        }

    )

    assert response.status_code == 200


# -----------------------------------------
# Test Invalid URL
# -----------------------------------------

def test_predict_invalid_url(client):

    response = client.post(

        "/predict",

        data={

            "url": "abcd"

        }

    )

    assert response.status_code == 200