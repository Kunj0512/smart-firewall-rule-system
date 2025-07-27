import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    df.dropna(inplace=True)
    df['label'] = df['action'].apply(lambda x: 1 if x == 'ALLOW' else 0)
    return df
