import pandas as pd
from sklearn.preprocessing import LabelEncoder

import warnings
warnings.filterwarnings('ignore')

def preprocessing():
    df = pd.read_csv('./data/raw/phishing_features.csv')

    df.drop('url',axis=1,inplace=True)

    df['tld'].fillna(df['tld'].mode()[0], inplace=True)

    df = df[df.duplicated() == 0]

    le = LabelEncoder()
    df['tld'] = le.fit_transform(df['tld'])

    df.to_csv('./data/processed/clean_data.csv',index=False)

preprocessing()