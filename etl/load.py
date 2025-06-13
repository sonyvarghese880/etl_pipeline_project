#def load_data(df, output_path):
#    """Save the DataFrame as a CSV file."""
#    df.to_csv(output_path, index=False)



import pandas as pd

def load_data(df: pd.DataFrame, output_path: str):
    """
    Saves the transformed dataframe to S3  in Parquet format.
    """
    df.to_parquet(output_path, engine='pyarrow', index=False)
    print(f"Data saved to: {output_path}")
