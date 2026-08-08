"""
feature_engineering.py
---------------------------------------
Feature Extraction for Phishing URL Detection
"""

import math
import re
import pandas as pd
from collections import Counter
from urllib.parse import urlparse, parse_qs


# ---------------------------------------------------
# Suspicious Words
# ---------------------------------------------------

SUSPICIOUS_WORDS = [
    "login",
    "signin",
    "verify",
    "secure",
    "account",
    "bank",
    "paypal",
    "update",
    "password",
    "confirm",
    "bonus",
    "gift",
    "wallet",
    "ebay",
    "amazon",
    "invoice",
    "free"
]


# ---------------------------------------------------
# URL Length
# ---------------------------------------------------

def url_length(url):
    return len(url)


# ---------------------------------------------------
# Number of Dots
# ---------------------------------------------------

def num_dots(url):
    return url.count(".")


# ---------------------------------------------------
# HTTPS
# ---------------------------------------------------

def has_https(url):
    return 1 if url.lower().startswith("https://") else 0


# ---------------------------------------------------
# IP Address
# ---------------------------------------------------

def has_ip(url):

    pattern = (
        r"^(?:http[s]?://)?"
        r"(\d{1,3}\.){3}\d{1,3}"
    )

    return 1 if re.search(pattern, url) else 0


# ---------------------------------------------------
# Number of Subdirectories
# ---------------------------------------------------

def num_subdirs(url):

    path = urlparse(url).path

    return len([x for x in path.split("/") if x])


# ---------------------------------------------------
# Number of Parameters
# ---------------------------------------------------

def num_params(url):

    query = urlparse(url).query

    return len(parse_qs(query))


# ---------------------------------------------------
# Suspicious Words
# ---------------------------------------------------

def suspicious_words(url):

    url = url.lower()

    count = 0

    for word in SUSPICIOUS_WORDS:

        if word in url:
            count += 1

    return count


# ---------------------------------------------------
# Top Level Domain
# ---------------------------------------------------

def tld(url):

    domain = urlparse(url).netloc.lower()
    enc = pd.read_csv("./data/external/encoded.csv")
    enc.set_index(enc['Unnamed: 0'],inplace=True)
    enc.drop("Unnamed: 0",axis=1,inplace=True)

    if domain.startswith("www."):

        domain = domain[4:]

    parts = domain.split(".")

    for part in parts:
        if part in enc.index:
            return enc.loc[part].iloc[0]
    else: return None


# ---------------------------------------------------
# Special Characters
# ---------------------------------------------------

def special_char_count(url):

    return len(re.findall(r"[^A-Za-z0-9]", url))


# ---------------------------------------------------
# Digits Count
# ---------------------------------------------------

def digits_count(url):

    return sum(c.isdigit() for c in url)


# ---------------------------------------------------
# Shannon Entropy
# ---------------------------------------------------

def entropy(url):

    counts = Counter(url)

    length = len(url)

    entropy = 0

    for count in counts.values():

        probability = count / length

        entropy -= probability * math.log2(probability)

    return round(entropy, 4)

def get_base_url(url):
    
    parsed = urlparse(url)

    return f"{parsed.scheme}://{parsed.netloc}"


# ---------------------------------------------------
# Main Feature Extraction
# ---------------------------------------------------

def extract_features(url):

    url = get_base_url(url)

    return {

        "url_length": url_length(url),

        "num_dots": num_dots(url),

        "has_https": has_https(url),

        "has_ip": has_ip(url),

        "num_subdirs": num_subdirs(url),

        "num_params": num_params(url),

        "suspicious_words": suspicious_words(url),

        "tld": tld(url),

        "special_char_count": special_char_count(url),

        "digits_count": digits_count(url),

        "entropy": entropy(url)

    }

