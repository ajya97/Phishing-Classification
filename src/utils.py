"""
utils.py
-----------------------------
Common utility functions
"""

import os
import joblib
import logging
import random
import numpy as np
import pandas as pd
from datetime import datetime


# ----------------------------------------------------
# Save Model
# ----------------------------------------------------

def save_model(model, path):
    """
    Save trained model.
    """
    joblib.dump(model, path)
    print(f"Model saved to: {path}")


# ----------------------------------------------------
# Load Model
# ----------------------------------------------------

def load_model(path):
    """
    Load trained model.
    """
    return joblib.load(path)


# ----------------------------------------------------
# Save DataFrame
# ----------------------------------------------------

def save_csv(df, path):
    """
    Save dataframe as CSV.
    """
    df.to_csv(path, index=False)


# ----------------------------------------------------
# Load CSV
# ----------------------------------------------------

def load_csv(path):
    """
    Load CSV file.
    """
    return pd.read_csv(path)

