# Next work

The main work now is to complete the records for all three drones with actual photos and flight videos. I will match the videos with their drone setups and record real flight times and ranges.

For the current large quadcopter I still need to verify the power module and battery current measurement, investigate why one ESC temperature channel is hotter than the others, and isolate the cause of the intermittent RF video loss.

I also want to add the exact motor, ESC, propeller, GNSS, RF and camera models, confirmed PX4 parameter exports, flight logs that are safe to share and more notes about tuning and flight behaviour.

I will update the pages as the testing continues instead of writing a final result before I have checked it.
## Control and filter validation

I also need to repeat a controlled flight with the revised PID and filter settings, verify the ESC RPM telemetry source, and compare raw gyro spectra and rate tracking with similar manoeuvres. I want to confirm the physical GNSS/IMU positions against the saved EKF2 offsets, and record the old and new values for each future parameter change. This is necessary before I can call the tuning complete.
