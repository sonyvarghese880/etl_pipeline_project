import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from etl.transform import transform_data

def test_transform_data():
    sample_data = pd.DataFrame({
        "trip_distance": [2.5, 0.0, 1.2, 3.0],
        "fare_amount": [10.5, 5.0, 0.0, 9.0],
        "passenger_count": [1, 2, 3, 1]
    })

    transformed_df = transform_data(sample_data)

    # Only rows with trip_distance > 0 and fare_amount > 0 should remain
    expected = sample_data[(sample_data['trip_distance'] > 0) & (sample_data['fare_amount'] > 0)]

    assert len(transformed_df) == len(expected)
    assert "trip_distance_km" in transformed_df.columns