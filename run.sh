#!/bin/bash

LOG_FILE="run_log.txt"

echo "Starting ETL Pipeline..." | tee $LOG_FILE

# Run main ETL pipeline
echo "Running main.py..." | tee -a $LOG_FILE
python main.py >> $LOG_FILE 2>&1

if [ $? -ne 0 ]; then
    echo "ETL pipeline failed. Check $LOG_FILE for details." | tee -a $LOG_FILE
    exit 1
else
    echo "ETL pipeline completed successfully." | tee -a $LOG_FILE
fi

# Run tests
echo "Running tests with pytest..." | tee -a $LOG_FILE
pytest >> $LOG_FILE 2>&1

if [ $? -ne 0 ]; then
    echo "Tests failed. Check $LOG_FILE for details." | tee -a $LOG_FILE
    exit 1
else
    echo "All tests passed successfully." | tee -a $LOG_FILE
fi

echo "ETL Pipeline and Tests Completed." | tee -a $LOG_FILE
