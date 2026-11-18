# Gyro vibration, filters and ESC RPM investigation

This was one of the more time-consuming parts of the PX4 work. I wanted to understand whether the vibration seen in the logs was actual motion, motor/propeller excitation, or noise passing into the control loop.

The measurements below come from two tests on 4 November 2026: an initial Acro test and a longer Stabilized test. I analysed high-rate gyro samples and onboard ESC reports. Since the tests used different flight modes, the results are useful for diagnosis but do not form a controlled A/B tuning comparison.

## What we found in the raw gyro

The main raw gyro energy was around **130 to 150 Hz**. A separate band was visible around **350 to 400 Hz**. The strong lower-frequency band was close to the motor shaft frequencies calculated from reported RPM.

| Axis | Initial Acro peak | Stabilized peak | 100–180 Hz band-power ratio, second/first |
| --- | ---: | ---: | ---: |
| Roll | 132.4 Hz | 137.9 Hz | 20.7× |
| Pitch | 131.6 Hz | 132.0 Hz | 3.8× |
| Yaw | 133.6 Hz | 140.2 Hz | 4.8× |

For the longer flight, the four reported median motor shaft frequencies were approximately 130.7, 149.5, 145.9 and 133.3 Hz. Shaft frequency is RPM / 60. Blade-passing frequency would be the shaft frequency multiplied by the number of blades, but the propeller blade count needs confirming before identifying the higher band as blade-passing vibration.

There was **no gyro clipping** in either log. The short log had two accelerometer clipping events in one sensor counter; the longer log had none in its final counters. This does not mean vibration was absent. Clipping and frequency-domain vibration are different checks.

## The ESC RPM problem

The ESC status flags showed four online channels, but ESC 2 and ESC 3 had missing or implausible RPM reports while motor commands were substantial. For a diagnostic check, we counted reports below 1,500 RPM when the corresponding normalized motor command exceeded 0.40.

| ESC channel | Initial Acro | Stabilized |
| --- | ---: | ---: |
| 1 | 0.01% | 0.56% |
| 2 | 19.59% | 10.40% |
| 3 | 25.49% | 14.95% |
| 4 | 0.25% | 1.12% |

Some RPM samples also had unrealistic spikes. These values should not be treated as the motors actually stopping, because the drone kept flying and the motor commands remained active. The likely area to investigate is ESC telemetry or decoding, including wiring, firmware, signal quality, output mapping and motor pole count.

The two earlier tests had `DSHOT_BIDIR_EN=1`. The revised controller test recorded `DSHOT_BIDIR_EN=0` and `DSHOT_TEL_CFG=103`. That is a configuration difference, not proof that the earlier RPM issue was fixed.

## What this means for notch filtering

A fixed notch at 60 Hz would not be supported by these spectra. The observed strong band was closer to 130–150 Hz and can move with motor speed. A dynamic notch may help a moving vibration peak, but the tracking source must be reliable and its actual performance must be checked in a log.

The earlier controller configurations had `IMU_GYRO_DNF_EN=0`, `IMU_GYRO_CUTOFF=40` Hz and `IMU_DGYRO_CUTOFF=20` Hz. The revised controller configuration had the dynamic notch enabled and the cutoffs raised to 60 Hz and 30 Hz. We have not yet completed the same high-rate spectral comparison for that later configuration, so I cannot claim that it removed the vibration.

## Controller tracking from the 4 November flights

The longer Stabilized log had approximate full-rate tracking RMSE values of 5.4 deg/s for roll, 6.3 deg/s for pitch and 5.7 deg/s for yaw. The shorter Acro log gave about 5.0, 3.0 and 3.5 deg/s over its available airborne data. The short log has sparse rate-setpoint logging, and the modes and manoeuvres differ, so these values are not evidence that one PID setting was better.

The longer log also showed persistently different average motor commands between two motor pairs. This can happen with centre-of-gravity offset, thrust differences, geometry or trim. I need the motor positions and physical setup before assigning a cause.

## How I want to continue

First inspect the frame, propellers, motor bearings and flight-controller mounting. Then verify reliable RPM telemetry from all four ESCs. After that, repeat controlled flights with the same manoeuvres and compare raw gyro spectra, filtered gyro noise, rate tracking, actuator effort and ESC temperatures. Only then make one filter or gain change at a time.

I am keeping the unresolved findings here because diagnosing them is part of the project, not something to hide from the final results.

[Controller explanation](px4-control-system.md) | [Recorded parameters](px4-tuning-history.md) | [Flight records](flight-records/README.md)
