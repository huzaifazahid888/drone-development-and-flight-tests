# PX4 PID tuning and flight-data analysis

I started by learning the PX4 control structure. The attitude controller gives a requested angular rate, and the rate PID controller tries to follow it using gyro feedback. The motor commands are generated after control allocation. I needed to understand these parts before deciding whether a problem came from the PID gains, vibration, motor response or the estimator.

## The way I approached tuning

1. **Save a working baseline.** I record the PX4 version, airframe, motor/ESC setup and QGroundControl parameters. I check calibration, motor order, motor direction and failsafes with propellers removed.
2. **Check mechanical vibration first.** I inspect the frame, motors, propellers and flight-controller mounting. A filter cannot repair a loose frame or damaged propeller.
3. **Fly a controlled baseline and save the ULog.** I compare the requested and measured roll, pitch and yaw rates, and look at gyro vibration, actuator outputs and ESC temperatures.
4. **Study the gyro frequency spectrum.** The 4 November logs showed a strong band near 130–150 Hz, not a fixed 60 Hz peak. I check whether vibration moves with RPM before choosing a notch approach.
5. **Check the feedback source.** The same logs had unreliable RPM reports on ESC 2 and 3. I do not want to use bad RPM telemetry to judge a dynamic filter.
6. **Change one group of parameters at a time.** For rate tuning I check `MC_*RATE_K/P/I/D/FF`; for attitude I check `MC_ROLL_P`, `MC_PITCH_P` and `MC_YAW_P`; for filtering I check the gyro and D-gyro cutoff and notch settings. I save the old value, new value and flight log.
7. **Compare the result, not just the number.** I check overshoot, settling, steady tracking, high-frequency motor effort, temperature and any warning. If the change makes things worse, I return to the last known working configuration.

The real parameter history shows that some flights were made with different gains, cutoffs and notch settings. However, we did not run a controlled one-variable experiment for every change. I am keeping that difference clear rather than claiming an improvement that the logs do not prove.

## Findings from the actual logs

The 4 November flights showed motor-frequency gyro vibration, with much higher roll vibration power in the longer flight. The later 14 November log had different controller gains and filtering, including enabled dynamic notch filtering. It also reported a high ESC 1 temperature, which needs an independent check. These are useful findings, but they do not mean the drone is completely tuned.

I also check the estimator, gyro/accelerometer clipping, motor saturation, battery voltage and current, and recorded failsafe messages. The raw logs are kept private until any location or system information is reviewed.

## Read the detailed records

- [How the PX4 control loops work](px4-control-system.md)
- [Actual parameters from three flight logs](px4-tuning-history.md)
- [130–150 Hz vibration and ESC RPM problem](px4-gyro-filter-investigation.md)
- [Initial Acro control test](flight-records/initial-acro-test.md)
- [Stabilized control test](flight-records/stabilized-control-test.md)
- [Revised controller test](flight-records/revised-control-test.md)
- [Parameter-change template](parameter-change-template.md)
- [ULog quick-check script](../scripts/README.md)
