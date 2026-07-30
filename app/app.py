"""
app.py
----------------------------
Flask Application for
Phishing URL Detection
"""

from flask import Flask, render_template, request
from src.predict import predict_url
from src.train import train_models
from src.evaluate import evaluate

app = Flask(__name__)


# -------------------------------------
# Home Page
# -------------------------------------

@app.route("/")
def home():

    return render_template("index.html")


# -------------------------------------
# Prediction
# -------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    url = request.form.get("url", "").strip()

    if url == "":

        return render_template(
            "result.html",
            error="Please enter a URL."
        )

    try:

        result = predict_url(url)

        return render_template(

            "result.html",

            url=result["url"],

            is_safe = result['is_safe'],

            prediction=result["prediction"],

            confidence=result["probability"]

        )

    except Exception as e:

        return render_template(

            "result.html",

            error=str(e)

        )


# -------------------------------------
# Train Model
# -------------------------------------

@app.route("/train")
def train():

    try:
        train_models()
        return {
            "status" : "train complete"
        }
    except Exception as e:
        return {
            "error" : str(e)
        }


@app.route("/evalute")
def evalute():

    try:
        evaluate()
        return {
            "status" : "evalution complete"
        }
    except Exception as e:
        return {
            "error" : str(e)
        }

