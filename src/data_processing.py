from __future__ import annotations
import pandas as pd
from .sensor_processing import validate_sensor_data, rolling_filter

def process_csv(input_path: str, output_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)
    validate_sensor_data(df)
    processed = rolling_filter(df)
    processed.to_csv(output_path, index=False)
    return processed
