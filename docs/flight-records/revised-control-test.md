# Revised controller and power-system test

**Date:** 14 November 2026 (UTC)  
**Platform:** Large PX4 quadcopter, FMUv6X family  
**Airborne duration:** Approximately 305 seconds

## Purpose

This flight provided data from a later controller and filter configuration. I used it to review the recorded settings, battery behaviour, ESC temperatures and estimator status.

## Measured results

| Measurement | Onboard result |
| --- | ---: |
| Approximate airborne time | 305 s |
| Battery type | 6S LiPo |
| Lowest reported pack voltage | 20.35 V |
| Maximum reported battery current | 122.36 A |
| Reported charge consumed | 6,639 mAh |
| Highest reported ESC temperature | 92°C on channel 1 |

The flight ended with normal disarming. The inspected recording did not report a battery failsafe or estimator fault.

These readings came from the onboard monitoring system, not an independently calibrated meter. I still need to check the power module scale and confirm the ESC temperature with a separate measurement.

## Controller and filtering

The roll and pitch rate multipliers were 1.4 and the yaw rate multiplier was 3.0. The roll and pitch D gains were about 0.000592 and 0.003. The attitude gains were 7.7 for roll, 7.0 for pitch and 5.0 for yaw.

The gyro cutoff was 60 Hz, the D-gyro cutoff was 30 Hz and dynamic gyro notch filtering was enabled. The saved GNSS/IMU offsets and ESC telemetry settings are documented in the [controller parameter history](../px4-tuning-history.md).

## What remains to be checked

This recording confirms the later configuration and highlights battery voltage sag and an unusually high ESC temperature reading. It does not establish that the revised PID or filter settings are better. A comparable flight with matched manoeuvres and verified RPM feedback is still needed.

A matching video will be added only after the recording and footage are confirmed to be from the same flight.

[Battery analysis](../battery-and-power.md) · [ESC temperature](../esc-temperature.md) · [Tuning history](../px4-tuning-history.md)
