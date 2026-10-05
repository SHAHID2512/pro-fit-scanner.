# Pro-Fit Scanner Architecture

## High-level flow

```text
Residual Limb
      |
      v
Multimodal Sensors
(ToF | Pressure | Load | IMU)
      |
      v
Data Acquisition Controller
      |
      v
USB / UART
      |
      v
Python Processing
  |      |       |
Validation Filtering Calibration
      |
      v
Digital Scan Dataset
      |
      v
3D Profile / Point Cloud
      |
      v
STL Export
      |
      v
CAD / Prosthetic Design
```

## Hardware layer
- ToF: non-contact distance/geometry measurements.
- Pressure: supporting local pressure measurements.
- Load cells: force/load measurements.
- IMU: orientation/motion information.

## Processing layer
1. Schema validation
2. Numeric validation
3. Rolling-median filtering
4. Summary generation
5. CSV export

## Geometry pipeline
```text
Calibrated range samples
        ↓
Sensor pose estimation
        ↓
3D coordinate transformation
        ↓
Point-cloud cleaning
        ↓
Surface reconstruction
        ↓
Mesh validation
        ↓
STL export
```

Sparse sample rows alone do not constitute a clinically accurate 3D model.

## Privacy
If real patient data is introduced:
- Use coded study IDs.
- Remove unnecessary identifiers.
- Never commit identifiable clinical records.
- Use appropriate access control and encryption.
