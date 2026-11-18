# Understanding the PX4 control system

I spent a lot of time understanding what PX4 is actually doing before changing gains. It is easy to change a PID value in QGroundControl, but it is more useful to know which loop uses that value and what the change should do to the aircraft.

## How the control loops are connected

For a multicopter, the simplified control path is:

```text
Pilot / flight mode / mission
            |
Position and velocity control (when the mode uses them)
            |
Attitude setpoint
            |
Attitude controller -> body rate setpoint (roll, pitch, yaw)
            |
Rate controller -> requested body torques
            |
Control allocation -> motor commands
            |
ESCs + motors + propellers -> actual motion
            |
IMU measurements -> filtering -> estimated/filtered rates
                              -> feedback to the rate controller

GNSS + IMU + barometer + other available sensors
            |
           EKF2 -> estimated attitude, position and velocity
                     -> feedback to the relevant outer loops
```

The inner **rate loop** controls angular velocity, usually in rad/s internally. The outer **attitude loop** works with orientation error and requests angular rates. Position and velocity control are used by the flight modes that need them. In Acro, the pilot mainly commands rates; in Stabilized, the attitude loop also matters. That is why comparing these two modes is not a controlled PID experiment.

## Rate PID and the parameters I checked

For roll, I worked with `MC_ROLLRATE_K`, `MC_ROLLRATE_P`, `MC_ROLLRATE_I`, `MC_ROLLRATE_D` and `MC_ROLLRATE_FF`. Pitch and yaw have the same family of parameters. In PX4, `K` is an overall multiplier for the rate PID terms. The separate P, I and D terms do different jobs:

- **P:** reacts to the current angular-rate error. More P can make the response stronger but can also amplify noise and oscillation.
- **I:** helps remove persistent rate error caused by trim, disturbances or an unbalanced load. It also needs saturation and anti-windup handling.
- **D:** reacts to the rate of change of the measured angular rate in the implemented controller. It can help damping, but gyro noise can make it costly for motors and ESCs.
- **FF:** rate-setpoint feedforward. It is not a replacement for feedback.

The attitude gains `MC_ROLL_P`, `MC_PITCH_P` and `MC_YAW_P` are not the same as the rate PID gains. They influence how strongly an attitude error is turned into a requested angular rate.

I also learned that a drone can look stable while hovering but still have poor rate tracking, excessive vibration, high motor effort or a weak response to fast commands. So I use the log rather than judging the tuning only from how it looks in the air.

## Filters are part of the control response

The gyro measurement contains the aircraft motion and unwanted vibration from motors, propellers and the frame. A low-pass filter reduces high-frequency noise but adds delay. A notch filter removes energy around a narrower frequency band. The D path also has its own filtering.

The important parameters in our FMUv6X logs include `IMU_GYRO_CUTOFF`, `IMU_DGYRO_CUTOFF`, `IMU_GYRO_NF0_FRQ`, `IMU_GYRO_NF1_FRQ` and the `IMU_GYRO_DNF_*` settings. I did not treat a lower cutoff or an enabled notch as automatically better. The result depends on the actual vibration spectrum and the response after filtering.

## Estimation is not the same as control

EKF2 estimates the vehicle state using IMU measurements and available aiding sensors. The controller then uses those estimates. The GNSS antenna position matters because an antenna away from the vehicle reference point has extra translational motion during rotation. This is a lever-arm effect, not a GPS measurement of yaw.

The exact offsets used in one recent log are recorded in [the parameter history](px4-tuning-history.md). The physical measurement and signed body axes still need to be checked before treating those numbers as final.

## What is actually implemented

These are PX4 controller algorithms and parameters that I configured, studied and tested. This repository does **not** claim that I wrote the PX4 attitude controller, EKF2 or control allocator from scratch. My work here is the hardware integration, configuration, tuning, flight testing and analysis of the results.

[Parameter history](px4-tuning-history.md) | [Vibration investigation](px4-gyro-filter-investigation.md) | [Tuning workflow](tuning-and-logs.md)
