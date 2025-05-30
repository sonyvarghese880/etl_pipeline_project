#!/bin/bash

LOG_FILE="run_log.txt"

echo "Starting ETL Pipeline..." | tee $LOG_FILE

# Function to run each step and handle errors
run_step() {
    step_name=$1
    script=$2

    echo "Running $step_name..." | tee -a $LOG_FILE
    python $script >> $LOG_FILE 2>&1

    if [ $? -ne 0 ]; then
        echo "$step_name failed. Check $LOG_FILE for details." | tee -a $LOG_FILE
        exit 1
    else
        echo "$step_name completed successfully." | tee -a $LOG_FILE
    fi
}

# Run ETL steps
run_step "Extract Step" "src/extract.py"
run_step "Transform Step" "src/transform.py"
run_step "Load Step" "src/load.py"

# Run tests
echo "Running Tests with pytest..." | tee -a $LOG_FILE
pytest >> $LOG_FILE 2>&1

if [ $? -ne 0 ]; then
    echo "Tests failed. Check $LOG_FILE for details." | tee -a $LOG_FILE
    exit 1
else
    echo "All tests passed successfully." | tee -a $LOG_FILE
fi

echo "ETL Pipeline and Tests Completed." | tee -a $LOG_FILE
