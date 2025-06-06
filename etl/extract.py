import pandas as pd

def extract_data(file_path='data/yellow_tripdata_2025-01.parquet'):
    """Read Parquet file and return a DataFrame."""  
    print(f"Reading data from {file_path} ...")                 
    data = pd.read_parquet(file_path)
    return data