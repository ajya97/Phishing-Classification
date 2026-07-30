"""
test_model.py
-------------------------------------
Unit Tests for ML Model
Run:
    pytest tests/test_model.py
"""

import os

from src.predict import load_model, predict_url
from src.config import MODEL_PATH


# ----------------------------------------------------
# Test Model File Exists
# ----------------------------------------------------

def test_model_file_exists():

    assert os.path.exists(MODEL_PATH)


# ----------------------------------------------------
# Test Model Loading
# ----------------------------------------------------

def test_model_loading():

    model = load_model()

    assert model is not None


# ----------------------------------------------------
# Test Prediction Output Type
# ----------------------------------------------------

def test_prediction_output():

    result = predict_url("https://www.google.com")

    assert isinstance(result, dict)


# ----------------------------------------------------
# Test Prediction Keys
# ----------------------------------------------------

def test_prediction_keys():

    result = predict_url("https://www.google.com")

    assert "url" in result
    assert "prediction" in result
    assert "probability" in result


# ----------------------------------------------------
# Test Prediction Class
# ----------------------------------------------------

def test_prediction_class():

    result = predict_url("https://www.google.com")

    assert result["prediction"] in [

        "Safe",
        "Phishing"

    ]


# ----------------------------------------------------
# Test Probability Range
# ----------------------------------------------------

def test_probability_range():

    result = predict_url("https://www.google.com")

    probability = result["probability"]

    assert probability >= 0
    assert probability <= 100


# ----------------------------------------------------
# Test Safe URL
# ----------------------------------------------------

def test_safe_url():

    result = predict_url(

        "https://www.wikipedia.org"

    )

    assert result is not None


# ----------------------------------------------------
# Test Phishing-like URL
# ----------------------------------------------------

def test_phishing_url():

    result = predict_url(

        "http://paypal-login-secure.xyz/login"

    )

    assert result is not None


# ----------------------------------------------------
# Test Long URL
# ----------------------------------------------------

def test_long_url():

    url = "https://example.com/" + "a" * 400

    result = predict_url(url)

    assert result is not None


# ----------------------------------------------------
# Test URL Returned
# ----------------------------------------------------

def test_url_returned():

    url = "https://google.com"

    result = predict_url(url)

    assert result["url"] == url
