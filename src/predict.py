"""
predict.py
--------------------
Load trained model and predict phishing URLs
"""

import joblib
import pandas as pd

from src.config import MODEL_PATH
from src.feature_engineering import extract_features


# -------------------------------------------------
# Load Model
# -------------------------------------------------

def load_model():

    model = joblib.load(MODEL_PATH)

    return model


# -------------------------------------------------
# Predict
# -------------------------------------------------

def predict_url(url):

    model = load_model()

    features = extract_features(url)

    df = pd.DataFrame([features])

    prediction = model.predict(df)[0]

    if hasattr(model, "predict_proba"):

        probability = model.predict_proba(df).max() * 100

    else:

        probability = None

    if prediction == 1:

        is_safe = False
        label = "Phishing"

    else:

        is_safe = True
        label = "Safe"

    return {

        "url": url,
        'is_safe': is_safe,
        "prediction": label,
        "probability": round(probability, 2) if probability else None

    }

