def transform_data(df):
    df = df.dropna()
    df['name'] = df['name'].str.upper()
    return df