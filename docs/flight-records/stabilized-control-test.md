# Stabilized control and vibration test

**Date:** 4 November 2026 (UTC)  
**Platform:** Large PX4 quadcopter, FMUv6X family  
**Flight mode:** Stabilized  
**Recorded data duration:** Approximately 396 seconds

## Purpose

This test was used to examine gyro vibration, rate tracking and ESC feedback during a longer recording. The roll and pitch rate gain multipliers were 1.1, while the base roll/pitch P, I and D values remained the same as in the earlier test. The gyro and D-gyro cutoffs were still 40 Hz and 20 Hz, with dynamic notch filtering disabled.

## Results

The strongest raw gyro vibration was around 132–140 Hz. The measured roll-axis power in the 100–180 Hz band was about 20.7 times the earlier Acro test. Gyro clipping remained at zero, while RPM reports from ESC channels 2 and 3 were still unreliable.

The approximate roll, pitch and yaw rate-tracking RMSE values were 5.4, 6.3 and 5.7 deg/s. A larger pitch manoeuvre late in the recording is worth reviewing for response delay and overshoot. GNSS aiding and downward range sensing were present. Battery status from this recording was not suitable for a reliable power analysis.

## What this means

Because this test used Stabilized mode and the earlier one used Acro, the observed differences cannot be attributed to the gain multiplier alone. This is a useful diagnostic record, not a controlled demonstration of better or worse PID tuning.

[Controller settings](../px4-tuning-history.md) · [Vibration analysis](../px4-gyro-filter-investigation.md)
