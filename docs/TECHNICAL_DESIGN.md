# Pro-Fit Scanner Technical Design Document

## 1. Purpose
Pro-Fit Scanner is a research prototype intended to digitize selected residual-limb measurements using a compact multimodal sensor platform and support a digital workflow for customized prosthetic development.

## 2. Design objectives
- Compact and portable measurement platform
- Multimodal measurement
- Timestamped digital data
- Basic validation and filtering
- Extensible software architecture
- Exportable data for CAD/3D workflows
- Low-cost prototype orientation

## 3. Proposed hardware

| Component | Role |
|---|---|
| VL53L5CX ToF | Distance/geometry sensing |
| MPU6050 | Orientation/motion |
| Load cells | Applied load |
| A301-type pressure sensors | Local pressure |
| ESP32/STM32 | Data acquisition |
| Battery | Portable power |
| USB/UART | Data transfer |

## 4. Functional requirements
- **FR-01:** Collect timestamped sensor measurements.
- **FR-02:** Reject missing required fields and invalid values.
- **FR-03:** Provide basic noise filtering.
- **FR-04:** Export processed CSV data.
- **FR-05:** Generate a machine-readable scan summary.
- **FR-06:** Keep sensor drivers and processing modular.

## 5. Data model
```text
timestamp_s
tof_mm
pressure_kpa
load_kg
imu_x
imu_y
imu_z
```

## 6. Processing algorithm
```text
START
 ↓
Read measurements
 ↓
Check required fields
 ↓
Check numeric values
 ↓
Reject invalid distance/load
 ↓
Apply rolling-median filter
 ↓
Generate summary
 ↓
Save processed data
 ↓
END
```

## 7. Calibration
A real implementation should document calibration date, reference instrument, reference values, measured values, correction and uncertainty/tolerance. Calibration constants should not be silently embedded in code.

## 8. Geometry reconstruction
A complete scanner needs distance measurements plus sensor pose. Each calibrated sample can be transformed into a 3D coordinate. Accumulated points can be filtered and reconstructed into a surface mesh before STL export.

## 9. Testing
### Unit
- Input validation
- Missing columns
- Invalid distance
- Negative load
- Filtering
- Summary statistics

### Integration
- CSV ingestion → filtering → export
- Firmware-like rows → parser → processing

### Hardware
- Sensor communication
- Calibration repeatability
- Mount stability
- Battery operation
- Serial communication

## 10. Risks

| Risk | Mitigation |
|---|---|
| Sensor noise | Filtering/calibration |
| Drift | Periodic calibration |
| Limb movement | IMU and controlled scanning |
| Poor surface response | Sensor-specific compensation |
| Incorrect geometry | Reference-object validation |
| Patient-data exposure | De-identification/access control |
| Mechanical instability | Rigid mounting |

## 11. Future work
- Point-cloud reconstruction
- Real-time 3D visualization
- Automated circumference extraction
- CAD parameter generation
- Wireless acquisition
- Automated scan-quality checks
- Clinical validation
