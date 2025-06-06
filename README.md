ETL Pipeline Project
--------------------

This is a simple yet scalable Python ETL pipeline that processes NYC Yellow Taxi trip data stored in Parquet format. It includes data cleaning, transformation, and loading to a CSV, with automated testing using pytest.

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
1. Install dependencies

    pip install -r requirements.txt

2. Give permission to run the shell script (first time only)

    chmod +x run.sh

3. Run the pipeline + tests

    ./run.sh

This:
- Runs the ETL pipeline via main.py
- Saves a log in run_log.txt
- Executes unit tests with pytest

ETL Breakdown
-----------------
- **Extract:** Loads a `.parquet` file into a DataFrame using `pyarrow`
- **Transform:** Filters out bad records, adds new columns (e.g., trip distance in km)
- **Load:** Exports cleaned data to CSV: `data/cleaned_data.csv`

Testing
-----------
Tests for the transformation logic are written using `pytest`.


Output
----------
You’ll get a cleaned CSV file in:

    data/cleaned_data.csv

And a log file with all pipeline/test results in:

    run_log.txt
