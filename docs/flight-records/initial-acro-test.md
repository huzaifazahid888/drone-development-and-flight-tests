# Initial Acro control test

**Date:** 4 November 2026 (UTC)  
**Platform:** Large PX4 quadcopter, FMUv6X family  
**Flight mode:** Acro  
**Recorded data duration:** Approximately 107 seconds

## Purpose

I used this test to inspect raw gyro vibration, ESC RPM feedback and the angular-rate controller. The roll and pitch rate gain multipliers were both 1.0, the gyro low-pass cutoff was 40 Hz and the D-gyro cutoff was 20 Hz. Dynamic gyro notch filtering was disabled.

## Results

The raw gyro showed a strong vibration peak around 132–134 Hz across the axes. No gyro clipping was reported. ESC channels 2 and 3 produced missing or implausible RPM values during periods of substantial motor command. The recorded rate-setpoint samples were sparse, so tracking measurements from this test are approximate.

The downward range measurements indicated operation close to the ground during the recorded period. GNSS aiding and range sensing were present, but this does not establish an autonomous landing test.

## What this means

The vibration frequency and RPM feedback quality need investigation before selecting a motor-tracking notch filter. The recorded parameters are historical values and should not be copied directly to another aircraft.

[Controller settings](../px4-tuning-history.md) · [Vibration analysis](../px4-gyro-filter-investigation.md)
