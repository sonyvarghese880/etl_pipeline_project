import pandas as pd

def extract_data(s3_path):
    """
    Extracts data from a Parquet file stored in S3 and returns a DataFrame.
    
    Parameters:
    - s3_path: Full S3 URI to the parquet file 

    Returns:
    - DataFrame with the loaded data
    """
    df = pd.read_parquet(s3_path, engine='pyarrow')
    return df