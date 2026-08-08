"""
train.py
---------
Train multiple ML models for phishing website detection
Select the best model based on validation accuracy
Save the best model
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier

from src.config import (
    DATA_PATH,
    MODEL_PATH,
    TARGET_COLUMN,
    RANDOM_STATE,
    TEST_SIZE
)
from src.utils import save_model,load_csv



# ----------------------------
# Load Dataset
# ----------------------------

def load_data():

    df = load_csv(DATA_PATH)

    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    return X, y

# ----------------------------
# Models
# ----------------------------

def get_models():

    return {

        "Random Forest": RandomForestClassifier(
            n_estimators=300,
            random_state=RANDOM_STATE
        ),

        "XGBoost": XGBClassifier(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=8,
            random_state=RANDOM_STATE,
            eval_metric="mlogloss"
        ),

        "LightGBM": LGBMClassifier(
            n_estimators=300,
            learning_rate=0.05,
            random_state=RANDOM_STATE
        ),

        "CatBoost": CatBoostClassifier(
            iterations=300,
            learning_rate=0.05,
            verbose=False,
            random_state=RANDOM_STATE
        )

    }


# ----------------------------
# Train Models
# ----------------------------

def train_models():

    X, y = load_data()

    X_train, X_valid, y_train, y_valid = train_test_split(

        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y

    )

    models = get_models()

    best_model = None
    best_name = None
    best_score = 0

    print("=" * 60)

    for name, model in models.items():

        print(f"Training : {name}")
        try:
            model.fit(X_train, y_train)
        except Exception as e:
            return e

        pred = model.predict(X_valid)

        score = accuracy_score(y_valid, pred)

        print(f"Accuracy : {score:.4f}")

        print("-" * 60)

        if score > best_score:

            best_score = score
            best_model = model
            best_name = name

    print()

    print("=" * 60)
    print(f"Best Model : {best_name}")
    print(f"Accuracy   : {best_score:.4f}")
    print("=" * 60)

    save_model(best_model, MODEL_PATH)

