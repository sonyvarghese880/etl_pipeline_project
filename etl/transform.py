def transform_data(df):
    df = df.copy()  #  Fix SettingWithCopyWarning
    df = df[(df['trip_distance'] > 0) & (df['fare_amount'] > 0)]

    df['trip_distance_km'] = df['trip_distance'] * 1.60934

    return df