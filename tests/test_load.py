import os
import sys

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pandas as pd
import boto3
from botocore.exceptions import NoCredentialsError
import pyarrow.parquet as pq
from etl.load import load_data






# Dummy S3 credentials should be set as environment variables for test
BUCKET_NAME = "yellow-taxi-nyc-data"
OUTPUT_KEY = "test/test_output.parquet"

def test_load_data_to_parquet(tmp_path):
    # Create a dummy DataFrame
    df = pd.DataFrame({
        "trip_distance": [2.5, 0.0],
        "fare_amount": [10.5, 5.0],
        "passenger_count": [1, 2]
    })

    # Temporary output file
    output_file = tmp_path / "dummy_output.parquet"

    # Call the load function
    load_data(df, str(output_file))

    # Assert file was written
    assert output_file.exists()

    # Load it back and assert values
    df_loaded = pd.read_parquet(str(output_file))
    assert df_loaded.equals(df)