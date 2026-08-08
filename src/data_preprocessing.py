import pandas as pd
from src.feature_engineering import extract_features

import warnings
warnings.filterwarnings('ignore')

def preprocessing():
    fdf = pd.read_csv('./data/raw/fraud_urls_20k.csv')
    pdf = pd.read_csv("./data/raw/legit_urls_20k.csv")
    df = pd.DataFrame(columns=extract_features(fdf.url[0]).keys())
    for i in range(len(pdf.url)+len(fdf.url)):
       if i < len(pdf.url):
           df.loc[len(df)] = extract_features(pdf.url[i])
       else:
           df.loc[len(df)] = extract_features(fdf.url[i-len(pdf.url)])
    df.drop_duplicates(inplace=True)

    df.to_csv('./data/processed/clean_data.csv',index=False)

preprocessing()