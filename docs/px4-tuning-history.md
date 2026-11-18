# PX4 controller tuning and parameter history

I kept the actual controller settings from three recorded flight tests so I could review how the configuration changed during development. These measurements came from the PX4 onboard parameter records of the large quadcopter, not from a generic tuning preset.

All three tests used the PX4 FMUv6X controller family. This is separate from the Pixhawk 2.4.8 hardware used during the first drone stage.

| Test | Date (UTC) | Flight context |
| --- | --- | --- |
| Initial Acro test | 4 Nov 2026 | About 107 s of recorded data |
| Stabilized control test | 4 Nov 2026 | About 396 s of recorded data |
| Revised controller test | 14 Nov 2026 | About 305 s airborne |

## Rate and attitude controller settings

| Parameter | Initial Acro | Stabilized | Revised |
| --- | ---: | ---: | ---: |
| `MC_ROLLRATE_K` | 1.0 | 1.1 | 1.4 |
| `MC_PITCHRATE_K` | 1.0 | 1.1 | 1.4 |
| `MC_YAWRATE_K` | 1.0 | 1.0 | 3.0 |
| `MC_ROLLRATE_P` | 0.102407 | 0.102407 | 0.102407 |
| `MC_ROLLRATE_I` | 0.129705 | 0.129705 | 0.129705 |
| `MC_ROLLRATE_D` | 0.000400 | 0.000400 | 0.000592 |
| `MC_PITCHRATE_P` | 0.114596 | 0.114596 | 0.114596 |
| `MC_PITCHRATE_I` | 0.144401 | 0.144401 | 0.144401 |
| `MC_PITCHRATE_D` | 0.000400 | 0.000400 | 0.003000 |
| `MC_YAWRATE_I` | 0.179794 | 0.179794 | 0.200000 |
| `MC_ROLL_P` | 6.5 | 6.5 | 7.7 |
| `MC_PITCH_P` | 6.5 | 6.5 | 7.0 |
| `MC_YAW_P` | 5.3402 | 5.3402 | 5.0 |

The base roll/pitch P and I rate gains remained the same across these three snapshots. The overall `K` multipliers increased, and the later flight also had different D and attitude gains. The pitch D change from 0.0004 to 0.003 is large enough that I want to inspect the motor effort, temperature and filtered gyro signal carefully. **A changed value is not proof that it improved the flight.**

The yaw rate P value stayed at about 0.178819, yaw D at about 0.000568, and all three rate feedforward values were zero in these logs.

## Gyro filtering and ESC interface

| Parameter | Initial Acro | Stabilized | Revised |
| --- | ---: | ---: | ---: |
| `IMU_GYRO_CUTOFF` (Hz) | 40 | 40 | 60 |
| `IMU_DGYRO_CUTOFF` (Hz) | 20 | 20 | 30 |
| `IMU_GYRO_DNF_EN` | 0 | 0 | 1 |
| `IMU_GYRO_DNF_MIN` (Hz) | 25 | 25 | 56 |
| `IMU_GYRO_DNF_BW` (Hz) | 15 | 15 | 30 |
| `IMU_GYRO_DNF_HMC` | 3 | 3 | 3 |
| `IMU_GYRO_NF0_FRQ` (Hz) | 0 | 0 | 0 |
| `IMU_GYRO_NF1_FRQ` (Hz) | 0 | 0 | 0 |
| `DSHOT_BIDIR_EN` | 1 | 1 | 0 |
| `DSHOT_TEL_CFG` | 0 | 0 | 103 |

The first two flights had dynamic notch disabled and both static notch centre frequencies at zero. In the 14 November snapshot the dynamic notch was enabled, with different minimum frequency and bandwidth. The gyro low-pass cutoff also increased from 40 to 60 Hz, and the D-path cutoff from 20 to 30 Hz.

Bidirectional DShot was enabled in the earlier logs and disabled in the later one. The later log also has a different ESC telemetry configuration. The log contains ESC reports, but their presence alone does not prove that every RPM value is valid. The actual telemetry wiring and source need checking.

## GNSS, IMU position and range sensor settings

| Parameter | Initial Acro | Stabilized | Revised |
| --- | ---: | ---: | ---: |
| `EKF2_GPS_CTRL` | 15 | 7 | 15 |
| `EKF2_RNG_CTRL` | 1 | 1 | 1 |
| `EKF2_GPS_POS_X` (m) | 0 | 0 | +0.07498 |
| `EKF2_GPS_POS_Y` (m) | 0 | 0 | 0 |
| `EKF2_GPS_POS_Z` (m) | 0 | 0 | -0.04602 |
| `EKF2_IMU_POS_X` (m) | 0 | 0 | -0.08998 |
| `EKF2_IMU_POS_Y` (m) | 0 | 0 | 0 |
| `EKF2_IMU_POS_Z` (m) | 0 | 0 | 0 |
| `MPC_LAND_SPEED` (m/s) | 0.7 | 0.7 | 0.7 |

I had estimated the antenna to be about 20 cm horizontally and 5 cm above the flight controller. In the latest saved configuration, the GPS X position is about +7.5 cm and the IMU X position about -9.0 cm. The difference is about **16.5 cm along body X**, with a GPS Z setting near -4.6 cm. This is useful to compare against the physical mounting, but it is not a replacement for measuring the actual centre of gravity and checking the PX4 body axes.

The older flights recorded GNSS position/velocity aiding and downward distance sensor data. They did **not** demonstrate a successful autonomous landing. The presence of `MPC_LAND_SPEED=0.7` is a parameter value, not evidence of an automatic landing test.

## What this history can and cannot tell us

These are **recorded snapshots**, not a step-by-step record of every adjustment made in QGroundControl. Several parameters changed between 4 and 14 November, so I cannot isolate which change caused a difference in flight behaviour. Even the two 4 November logs used different flight modes.

To make a proper tuning comparison, I need a matching flight log, the exact old and new parameters, similar test manoeuvres, and notes about vibration, tracking, oscillation and ESC temperature. I will keep future changes in [the parameter-change template](parameter-change-template.md).

The raw flight recordings are kept private because they may contain GNSS positions and system information. Selected parameters are available in [configuration snapshots](../configs/README.md). **These are historical measurements, not a flight-ready configuration.**
