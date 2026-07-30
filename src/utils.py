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
# Create Directory
# ----------------------------------------------------

def create_directory(path):
    """
    Create directory if it does not exist.
    """
    os.makedirs(path, exist_ok=True)


# ----------------------------------------------------
# Save Model
# ----------------------------------------------------

def save_model(model, path):
    """
    Save trained model.
    """
    create_directory(os.path.dirname(path))
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
    create_directory(os.path.dirname(path))
    df.to_csv(path, index=False)


# ----------------------------------------------------
# Load CSV
# ----------------------------------------------------

def load_csv(path):
    """
    Load CSV file.
    """
    return pd.read_csv(path)


# ----------------------------------------------------
# Set Random Seed
# ----------------------------------------------------

def set_seed(seed=42):
    """
    Set random seed for reproducibility.
    """
    random.seed(seed)
    np.random.seed(seed)


# ----------------------------------------------------
# Logger
# ----------------------------------------------------

def setup_logger(log_file="logs/project.log"):

    create_directory(os.path.dirname(log_file))

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    return logging.getLogger()


# ----------------------------------------------------
# Print Section
# ----------------------------------------------------

def print_header(title):

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ----------------------------------------------------
# Current Time
# ----------------------------------------------------

def current_time():

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ----------------------------------------------------
# File Exists
# ----------------------------------------------------

def file_exists(path):

    return os.path.isfile(path)


# ----------------------------------------------------
# Display Dataset Info
# ----------------------------------------------------

def dataset_info(df):

    print_header("Dataset Information")

    print("Rows :", df.shape[0])
    print("Columns :", df.shape[1])

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nData Types")
    print(df.dtypes)


# ----------------------------------------------------
# Memory Usage
# ----------------------------------------------------

def memory_usage(df):

    mem = df.memory_usage(deep=True).sum()

    return round(mem / 1024**2, 2)


# ----------------------------------------------------
# Class Distribution
# ----------------------------------------------------

def class_distribution(target):

    print(target.value_counts())

    print()

    print(target.value_counts(normalize=True) * 100)