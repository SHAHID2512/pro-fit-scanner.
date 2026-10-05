from __future__ import annotations
import pandas as pd

REQUIRED_COLUMNS = [
    "timestamp_s", "tof_mm", "pressure_kpa", "load_kg",
    "imu_x", "imu_y", "imu_z"
]

def validate_sensor_data(df: pd.DataFrame) -> None:
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    if df.empty:
        raise ValueError("Sensor data is empty.")
    for col in REQUIRED_COLUMNS:
        if not pd.api.types.is_numeric_dtype(df[col]):
            raise TypeError(f"Column '{col}' must be numeric.")
    if (df["tof_mm"] <= 0).any():
        raise ValueError("ToF distance must be positive.")
    if (df["load_kg"] < 0).any():
        raise ValueError("Load cannot be negative.")

def rolling_filter(df: pd.DataFrame, window: int = 3) -> pd.DataFrame:
    """Apply a centered rolling median to measurement channels."""
    out = df.copy()
    for col in ["tof_mm", "pressure_kpa", "load_kg", "imu_x", "imu_y", "imu_z"]:
        out[col] = out[col].rolling(window, center=True, min_periods=1).median()
    return out

def summarize(df: pd.DataFrame) -> dict:
    validate_sensor_data(df)
    return {
        "samples": int(len(df)),
        "duration_s": float(df["timestamp_s"].iloc[-1] - df["timestamp_s"].iloc[0]),
        "tof_min_mm": float(df["tof_mm"].min()),
        "tof_max_mm": float(df["tof_mm"].max()),
        "pressure_mean_kpa": float(df["pressure_kpa"].mean()),
        "load_max_kg": float(df["load_kg"].max()),
    }
