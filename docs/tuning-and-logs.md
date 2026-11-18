# PID, filters and ULog checks

As the flights progressed I started checking the rate and attitude behaviour in PX4. I looked at how the controller responds to command inputs, motor output, IMU vibration and whether filtering reduces noise without adding too much delay.

The main points I have been studying include static notch filters, dynamic notch filtering, gyro low-pass filtering, D-term filtering, ESC RPM telemetry and the difference between real motor vibration and noise caused by the measurement or signal path.

For log analysis I inspect estimator status, gyro and accelerometer clipping, motor and ESC readings, rate setpoints versus measured rates, battery voltage and current and any recorded failsafe messages.

I do not want to publish recommended gains as if they were verified on all of my drones. Any final parameter export belongs with its specific airframe and the flight used to check it.

[Flight record](flight-records/12_43_50.md) · [ULog quick-check script](../scripts/README.md)