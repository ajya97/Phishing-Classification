"""
evaluate.py
--------------------------------
Evaluate trained phishing detection model
"""

import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay,
    RocCurveDisplay
)

from sklearn.model_selection import train_test_split

from src.config import (
    DATA_PATH,
    TARGET_COLUMN,
    MODEL_PATH,
    TEST_SIZE,
    RANDOM_STATE,
    REPORT_PATH
)
from src.utils import load_csv,load_model


# ---------------------------------------
# Load Data
# ---------------------------------------

def load_data():

    df = load_csv(DATA_PATH)

    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    return train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y
    )



# ---------------------------------------
# Evaluate
# ---------------------------------------

def evaluate():

    os.makedirs(REPORT_PATH, exist_ok=True)

    X_train, X_test, y_train, y_test = load_data()

    model = load_model(MODEL_PATH)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    precision = precision_score(
        y_test,
        predictions,
        average="weighted"
    )

    recall = recall_score(
        y_test,
        predictions,
        average="weighted"
    )

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted"
    )

    print("=" * 50)
    print("Model Evaluation")
    print("=" * 50)

    print(f"Accuracy  : {accuracy:.4f}")
    print(f"Precision : {precision:.4f}")
    print(f"Recall    : {recall:.4f}")
    print(f"F1 Score  : {f1:.4f}")

    print("=" * 50)

    # ------------------------------------
    # Classification Report
    # ------------------------------------

    report = classification_report(
        y_test,
        predictions
    )

    print(report)

    with open(
        os.path.join(REPORT_PATH, "classification_report.txt"),
        "w"
    ) as f:

        f.write(report)

    # ------------------------------------
    # Confusion Matrix
    # ------------------------------------

    cm = confusion_matrix(
        y_test,
        predictions
    )

    disp = ConfusionMatrixDisplay(cm)

    disp.plot()

    plt.savefig(
        os.path.join(
            REPORT_PATH,
            "confusion_matrix.png"
        )
    )

    plt.close()

    # ------------------------------------
    # ROC Curve
    # ------------------------------------

    if hasattr(model, "predict_proba"):

        RocCurveDisplay.from_estimator(
            model,
            X_test,
            y_test
        )

        plt.savefig(
            os.path.join(
                REPORT_PATH,
                "roc_curve.png"
            )
        )

        plt.close()

    # ------------------------------------
    # Save Metrics
    # ------------------------------------

    metrics = pd.DataFrame({

        "Metric": [

            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score"

        ],

        "Score": [

            accuracy,
            precision,
            recall,
            f1

        ]

    })

    metrics.to_csv(

        os.path.join(
            REPORT_PATH,
            "evaluation_metrics.csv"
        ),

        index=False

    )

    print()

    print("Reports Saved Successfully")

