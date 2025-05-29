from extract import extract_data
from transform import transform_data
from load import load_data

if __name__ == '__main__':
    raw_data = extract_data('data/input_data.csv')
    cleaned_data = transform_data(raw_data)
    load_data(cleaned_data, 'etl.db')
    print("ETL process completed.")