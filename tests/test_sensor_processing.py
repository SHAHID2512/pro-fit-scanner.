import pandas as pd
import pytest
from src.sensor_processing import validate_sensor_data, rolling_filter, summarize

def sample_df():
    return pd.DataFrame({
        "timestamp_s": [0.0, 0.1, 0.2],
        "tof_mm": [180.0, 181.0, 182.0],
        "pressure_kpa": [10.0, 11.0, 12.0],
        "load_kg": [4.0, 4.2, 4.4],
        "imu_x": [0.01, 0.02, 0.03],
        "imu_y": [0.00, 0.01, 0.02],
        "imu_z": [0.98, 0.99, 1.00],
    })

def test_validation_accepts_valid_data():
    validate_sensor_data(sample_df())

def test_validation_rejects_missing_column():
    with pytest.raises(ValueError):
        validate_sensor_data(sample_df().drop(columns=["tof_mm"]))

def test_validation_rejects_negative_load():
    df = sample_df()
    df.loc[0, "load_kg"] = -1
    with pytest.raises(ValueError):
        validate_sensor_data(df)

def test_filter_preserves_row_count():
    assert len(rolling_filter(sample_df())) == 3

def test_summary():
    result = summarize(sample_df())
    assert result["samples"] == 3
    assert result["tof_min_mm"] == 180.0
    assert result["tof_max_mm"] == 182.0
