# Project updates

## November 2026

I organized my quadcopter work into three stages: small drone, mid-size drone and the current 736 × 615 mm drone.

I added the current PX4 setup notes, battery and ESC observations and a recorded flight-test analysis. I also prepared the media folders and test records for adding photos and videos.

The hardware specifications, flight ranges and unresolved RF and temperature issues will be updated when the real evidence is added.

## 19 November 2026

- Added a detailed PX4 controller explanation, including rate PID, attitude, filters and EKF2.
- Extracted and compared actual control/filter/EKF2 settings from three FMUv6X ULogs.
- Documented the 130–150 Hz gyro vibration and ESC 2/3 RPM telemetry issues.
- Added the two 4 November flight records and selected historical parameter snapshots.
- Linked the tuning work from the main README and large-drone page.

## Drone photos and technical documentation

I added the three drone overview photos with white backgrounds, linked them from the main README and recorded the first Pixhawk 2.4.8 setup and the later STM32H7-based Pixhawk development stage. The exact model numbers for the later controllers still need to be checked from the hardware.

## Flight-test documentation update

I replaced raw recording names in the public documentation with descriptive test titles. The measured findings and recorded controller settings remain available, but each result is now explained by the test purpose and observation rather than a file identifier.
