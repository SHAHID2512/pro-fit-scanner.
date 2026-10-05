from __future__ import annotations
import argparse
import json
from pathlib import Path
from .data_processing import process_csv
from .sensor_processing import summarize

def main() -> None:
    parser = argparse.ArgumentParser(description="Pro-Fit Scanner reference pipeline")
    parser.add_argument("--input", required=True, help="Input sensor CSV")
    parser.add_argument("--output", default="output", help="Output directory")
    args = parser.parse_args()
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    processed_path = output_dir / "processed_sensor_data.csv"
    processed = process_csv(args.input, str(processed_path))
    summary_path = output_dir / "scan_summary.json"
    summary_path.write_text(json.dumps(summarize(processed), indent=2))
    print(f"Processed data: {processed_path}")
    print(f"Summary: {summary_path}")

if __name__ == "__main__":
    main()
