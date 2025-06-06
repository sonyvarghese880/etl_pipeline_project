import pandas as pd

def extract_data(filepath):
    """Read Parquet file and return a DataFrame."""
    data = pd.read_parquet(file_path)
    return data