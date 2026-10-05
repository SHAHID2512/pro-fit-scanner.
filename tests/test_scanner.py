from pathlib import Path
from src.data_processing import process_csv

def test_process_csv(tmp_path):
    source = Path("data/sample_sensor_data.csv")
    destination = tmp_path / "processed.csv"
    result = process_csv(str(source), str(destination))
    assert destination.exists()
    assert len(result) > 0
    assert "tof_mm" in result.columns
