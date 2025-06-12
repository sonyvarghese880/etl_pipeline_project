from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def main():
    input_path = "s3://yellow-taxi-nyc-data/raw/yellow_tripdata_2025-01.parquet"
    #output_path = "data/cleaned_data.csv"
    output_path = "s3://yellow-taxi-nyc-data/processed/yellow_tripdata_2025-01-cleaned.parquet"

    

    # Step 1: Read file
    df = extract_data(input_path)

    # Step 2: Clean the data
    df_clean = transform_data(df)

    # Step 3: Save to CSV
    load_data(df_clean, output_path)

if __name__ == "__main__":
    main()