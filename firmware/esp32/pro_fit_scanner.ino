/*
  Pro-Fit Scanner - ESP32 acquisition skeleton.
  Demonstration values are used below; replace them with real sensor drivers.
*/

const unsigned long SAMPLE_INTERVAL_MS = 100;
unsigned long lastSample = 0;

void setup() {
  Serial.begin(115200);
  delay(500);
  Serial.println("timestamp_ms,tof_mm,pressure_kpa,load_kg,imu_x,imu_y,imu_z");
  // Initialize selected sensors here.
}

void loop() {
  unsigned long now = millis();

  if (now - lastSample >= SAMPLE_INTERVAL_MS) {
    lastSample = now;

    float tof_mm = 182.0;
    float pressure_kpa = 12.0;
    float load_kg = 4.0;
    float imu_x = 0.02;
    float imu_y = 0.01;
    float imu_z = 0.98;

    Serial.print(now); Serial.print(",");
    Serial.print(tof_mm, 2); Serial.print(",");
    Serial.print(pressure_kpa, 2); Serial.print(",");
    Serial.print(load_kg, 2); Serial.print(",");
    Serial.print(imu_x, 3); Serial.print(",");
    Serial.print(imu_y, 3); Serial.print(",");
    Serial.println(imu_z, 3);
  }
}
