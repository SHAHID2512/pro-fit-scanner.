# Pro-Fit Scanner

A compact multimodal biomedical scanning prototype for collecting residual-limb geometry and complementary sensor measurements to support customized prosthetic development.

> **Status:** Prototype / research demonstrator. This repository contains an open-source reference implementation and synthetic sample data. It is **not a clinically validated medical device** and must not be used as the sole basis for clinical decisions or prosthetic fabrication.

## Problem
Manual residual-limb measurement and casting can be time-consuming and may require repeated adjustments. Pro-Fit Scanner explores a portable digital workflow combining non-contact distance sensing with pressure, load and orientation measurements.

## Workflow
**Scan → sensor data → calibration/filtering → digital limb profile → STL → customized prosthetic design**

## Architecture
```text
Residual Limb
     ↓
ToF | Pressure | Load | IMU
     ↓
Data Acquisition MCU
     ↓
USB / UART
     ↓
Python Processing
 ├─ validation
 ├─ filtering
 └─ calibration
     ↓
Digital Limb Profile
     ↓
STL / CAD
     ↓
Customized Prosthetic Design
```

## Reference hardware
- VL53L5CX ToF distance sensor
- MPU6050 IMU
- Load cells with suitable amplifier/ADC
- A301-type pressure sensors
- ESP32 or STM32-class controller
- Battery and USB/UART interface

The software separates acquisition from processing so sensor drivers can be replaced without rewriting the analysis pipeline.

## Repository structure
```text
pro-fit-scanner/
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── requirements.txt
├── data/
│   └── sample_sensor_data.csv
├── docs/
│   ├── TECHNICAL_DESIGN.md
│   ├── ARCHITECTURE.md
│   ├── TEST_CASES.md
│   └── architecture_diagram.svg
├── firmware/
│   └── esp32/
│       └── pro_fit_scanner.ino
├── src/
│   ├── __init__.py
│   ├── sensor_processing.py
│   ├── data_processing.py
│   └── scanner.py
└── tests/
    ├── test_sensor_processing.py
    └── test_scanner.py
```

## Setup

### Requirements
- Python 3.10+
- pip
- Optional: Arduino IDE
- Optional: ESP32/STM32 hardware

### 1. Clone
```bash
git clone https://github.com/YOUR-USERNAME/pro-fit-scanner.git
cd pro-fit-scanner
```

### 2. Virtual environment
```bash
python -m venv .venv
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Windows:
```powershell
.venv\Scripts\activate
```

### 3. Install
```bash
pip install -r requirements.txt
```

### 4. Environment variables
Copy `.env.example` to `.env`:
```text
SERIAL_PORT=COM3
BAUD_RATE=115200
DATA_PATH=data/sample_sensor_data.csv
OUTPUT_PATH=output
```

The sample pipeline works without hardware.

## Run
```bash
python -m src.scanner --input data/sample_sensor_data.csv --output output
```

This creates:
- `output/processed_sensor_data.csv`
- `output/scan_summary.json`

## Test
```bash
pytest -q
```

## Sample data
`data/sample_sensor_data.csv` contains **synthetic/non-patient data**.

| Column | Meaning |
|---|---|
| timestamp_s | Measurement time |
| tof_mm | Example distance |
| pressure_kpa | Example pressure |
| load_kg | Example load |
| imu_x/y/z | IMU axes |

## Firmware
`firmware/esp32/pro_fit_scanner.ino` demonstrates the CSV acquisition protocol. It uses demonstration values and should be connected to the actual sensor drivers for a hardware build.

Output format:
```text
timestamp_ms,tof_mm,pressure_kpa,load_kg,imu_x,imu_y,imu_z
```

## Technical documentation
- [Technical Design](docs/TECHNICAL_DESIGN.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Test Cases](docs/TEST_CASES.md)
- [Architecture Diagram](docs/architecture_diagram.svg)

## Limitations
- Not clinically validated.
- Sample data is synthetic.
- Sparse sensor rows alone do not constitute a clinically accurate 3D model.
- Accuracy depends on sensor mounting, calibration, surface properties and environment.

## Safety
This repository is for engineering research and prototyping. Before real-world clinical deployment, qualified teams should validate accuracy, repeatability, electrical safety, patient-contact materials, cybersecurity and applicable regulatory requirements.

## License
MIT License. See [LICENSE](LICENSE).
