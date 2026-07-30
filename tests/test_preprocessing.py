"""
test_preprocessing.py
----------------------------------------
Unit Tests for Data Preprocessing

Run:
    pytest tests/test_preprocessing.py
"""

import os
import pandas as pd

from config import DATA_PATH, TARGET_COLUMN
from src.data_preprocessing import preprocess_data


# ----------------------------------------------------
# Test Dataset Exists
# ----------------------------------------------------

def test_dataset_exists():

    assert os.path.exists(DATA_PATH)


# ----------------------------------------------------
# Test Dataset Loading
# ----------------------------------------------------

def test_dataset_loading():

    df = pd.read_csv(DATA_PATH)

    assert df is not None

    assert len(df) > 0


# ----------------------------------------------------
# Test Preprocessing Returns DataFrame
# ----------------------------------------------------

def test_preprocess_returns_dataframe():

    df = preprocess_data()

    assert isinstance(df, pd.DataFrame)


# ----------------------------------------------------
# Test Dataset Not Empty
# ----------------------------------------------------

def test_dataset_not_empty():

    df = preprocess_data()

    assert len(df) > 0


# ----------------------------------------------------
# Test Missing Values
# ----------------------------------------------------

def test_no_missing_values():

    df = preprocess_data()

    assert df.isnull().sum().sum() == 0


# ----------------------------------------------------
# Test Duplicate Rows
# ----------------------------------------------------

def test_no_duplicate_rows():

    df = preprocess_data()

    assert df.duplicated().sum() == 0


# ----------------------------------------------------
# Test Target Column Exists
# ----------------------------------------------------

def test_target_column_exists():

    df = preprocess_data()

    assert TARGET_COLUMN in df.columns


# ----------------------------------------------------
# Test Feature Count
# ----------------------------------------------------

def test_feature_count():

    df = preprocess_data()

    assert len(df.columns) >= 2


# ----------------------------------------------------
# Test URL Column Exists
# ----------------------------------------------------

def test_url_column_exists():

    df = preprocess_data()

    assert "url" in df.columns


# ----------------------------------------------------
# Test Label Values
# ----------------------------------------------------

def test_label_values():

    df = preprocess_data()

    labels = df[TARGET_COLUMN].unique()

    assert len(labels) >= 2


# ----------------------------------------------------
# Test URL Data Type
# ----------------------------------------------------

def test_url_datatype():

    df = preprocess_data()

    assert df["url"].dtype == object


# ----------------------------------------------------
# Test Empty URLs
# ----------------------------------------------------

def test_no_empty_urls():

    df = preprocess_data()

    assert (df["url"].str.strip() != "").all()


# ----------------------------------------------------
# Test URL Starts with HTTP
# ----------------------------------------------------

def test_urls_have_protocol():

    df = preprocess_data()

    valid = df["url"].str.startswith(
        ("http://", "https://")
    )

    assert valid.all()