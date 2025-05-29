import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from transform import transform_data  

import pandas as pd

def test_transform_data():
    df = pd.DataFrame({
        'id': [1, 2],
        'name': ['alice', 'bob'],
        'age': [30, 25],
        'city': ['New York', 'LA']
    })

    result = transform_data(df)
    assert result['name'].tolist() == ['ALICE', 'BOB']