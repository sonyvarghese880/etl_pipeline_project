ETL Pipeline Project
--------------------

This is a simple yet scalable Python ETL pipeline that processes NYC Yellow Taxi trip data stored in Parquet format. It includes data cleaning, transformation, loads the cleaned data to Amazon S3 in Parquet format, and with automated testing using pytest.

Folder Structure
----------------

etl_pipeline_project/
├── etl/
│   ├── extract.py           # Reads Parquet file
│   ├── transform.py         # Cleans and transforms data
│   └── load.py              # Saves cleaned data
├── tests/
│   └── test_transform.py    # Unit test for transform logic
├── data/
│   └── yellow_tripdata_2023-01.parquet  # Sample input file
├── main.py                  # Main pipeline script calling extract, transform, load
├── run.sh                   # Bash script to automate running pipeline + tests
├── requirements.txt         # Dependencies
└── README.md                # Project overview (this file)

How to Run
--------------
 Ensure you have Python 3.8+ and `pyarrow` installed:
bash
pip install -r requirements.txt

2. Place your raw Parquet file in S3 (e.g., `s3://yellow-taxi-nyc-data/raw/yellow_tripdata_2025-01.parquet`).

3. Modify main.py to reference your S3 or local path.

4. Run the pipeline:
bash
python main.py

This:
- Runs the ETL pipeline via main.py
- Saves a log in run_log.txt
- Executes unit tests with pytest

ETL Breakdown
-----------------
- Extracts raw Parquet data
- Transforms: filters rows, converts miles to kilometers
- Loads cleaned data to S3 as `.parquet`

Testing
-----------
Tests for the transformation logic are written using `pytest`.


S3 Output Example
------------------
s3://yellow-taxi-nyc-data/cleaned/cleaned_data.parquet


And a log file with all pipeline/test results in:

  run_log.txt

Note:
Make sure AWS credentials are configured properly to allow S3 read/write operations.

