# Drone Development and Flight Tests

I started working with a small quadcopter to understand the hardware and basic flight configuration. After the first tests, I moved to a mid-size drone and then to a larger quadcopter with a frame measuring about 736 mm × 615 mm. I made this repository to keep these three stages together, along with the actual hardware photos, flight videos, PX4 configurations and results from testing.

My work here includes motor and ESC configuration, Pixhawk and PX4 setup, QGroundControl calibration, GNSS and EKF2, PID and filter tuning, battery monitoring, and flight log analysis. I have also been working on a sight/camera system where video and MAVLink telemetry use the same RF link.

This is an ongoing project. Some tests are completed and some problems still need checking. I will add the original photos and flight videos as I sort them.

## Development photos

The three photos below show how the drone hardware changed during development. I kept the original components and wiring visible while preparing white-background images for the repository.

| Small quadcopter | Mid-size quadcopter | Current large quadcopter |
| :---: | :---: | :---: |
| ![Small quadcopter](media/photos/small-drone-overview.jpg) | ![Mid-size quadcopter](media/photos/mid-size-drone-overview.jpg) | ![Large quadcopter](media/photos/large-drone-overview.jpg) |
| Early prototype | Pixhawk-based development and sensor integration | 736 × 615 mm platform |

## Drone development

| Stage | Drone | Work |
| --- | --- | --- |
| 1 | [Small quadcopter](vehicles/01-small-drone/README.md) | Initial setup, motor directions, calibration and basic flights |
| 2 | [Mid-size quadcopter](vehicles/02-mid-size-drone/README.md) | Next airframe, configuration and testing |
| 3 | [Large quadcopter, 736 × 615 mm](vehicles/03-large-drone/README.md) | Current work with PX4, battery/ESC logs, GNSS and video telemetry |

**Photos:** The three overview photos are now added. I will add more detailed hardware pictures and flight videos after sorting the original files.

## Work and testing

The first work was mostly hardware assembly and learning how the flight controller handles motor order, direction, frame setup and sensor calibration. On the later drones I started spending more time on GNSS position estimation, the difference between the antenna and the centre of gravity, vibration, rate and attitude control and checking ULog files after flights.

On the current large drone I am also looking at battery voltage sag, current measurements, ESC temperatures, and interruptions in the live video sent over the same RF link as telemetry. I have kept these issues in the documentation since they are still useful parts of the testing.

## PX4 control and tuning findings

A large part of this project was understanding PX4's cascaded attitude and rate controllers and learning how to tune them using actual flight data. I checked PID gains, gyro filtering, motor RPM telemetry, GNSS/EKF2 settings and how these affect the behaviour of the drone. I also kept the problems we found, including strong motor-frequency vibration and unreliable RPM reports on some ESC channels.

The [parameter history](docs/px4-tuning-history.md) contains real settings extracted from three FMUv6X logs recorded on 4 and 14 November 2026. It shows the changes in rate gains, D terms, attitude gains, gyro cutoffs, dynamic notch settings, DShot telemetry and GNSS offsets. These are historical records, not universal tuning recommendations.

[How PX4 control works](docs/px4-control-system.md) · [Actual parameter changes](docs/px4-tuning-history.md) · [Gyro vibration and ESC RPM findings](docs/px4-gyro-filter-investigation.md) · [Tuning workflow](docs/tuning-and-logs.md)

## Flight videos and test records

I will add actual videos from different flights and ranges. Each flight will have its own record with the drone used, test conditions and the result. I will only write a flight distance or range when it has been checked from a record or confirmed separately.

| Test | Drone | Video filename to add | Record |
| --- | --- | --- | --- |
| Initial flight tests | Small | `small-drone-flight-01.mp4` | [Small drone](vehicles/01-small-drone/README.md) |
| Development flights | Mid-size | `mid-size-drone-flight-01.mp4` | [Mid-size drone](vehicles/02-mid-size-drone/README.md) |
| Large drone flight | Large | `large-drone-flight-01.mp4` | [Large drone](vehicles/03-large-drone/README.md) |
| PX4 log `12_43_50.ulg` | Large, if confirmed from the matching flight | `12_43_50-flight.mp4` | [Log analysis](docs/flight-records/12_43_50.md) |

These video filenames are reserved for files I will upload later. They are not links to videos that already exist.

[Photo names](media/photos/README.md) · [Video names](media/videos/README.md) · [Flight record template](docs/flight-records/TEMPLATE.md)

## Documentation

- [Hardware setup](docs/hardware.md)
- [PX4 and QGroundControl calibration](docs/setup-and-calibration.md)
- [GNSS and EKF2](docs/gnss-and-ekf2.md)
- [PX4 controller architecture](docs/px4-control-system.md)
- [PX4 tuning and parameter history](docs/px4-tuning-history.md)
- [Gyro filtering, vibration and ESC RPM investigation](docs/px4-gyro-filter-investigation.md)
- [PID tuning workflow and flight logs](docs/tuning-and-logs.md)
- [Battery and power measurements](docs/battery-and-power.md)
- [ESC temperature checks](docs/esc-temperature.md)
- [RF video and telemetry](docs/video-and-telemetry.md)
- [Preflight checklist](docs/preflight-checklist.md)
- [Next work](docs/next-work.md)

## Repository structure

```text
vehicles/           Small, mid-size and large drone records
docs/               Setup, calibration, testing and flight notes
configs/            Recorded parameter information
media/photos/       Real photos to be uploaded
media/videos/       Flight videos and video links to be uploaded
logs/               Notes about raw PX4 ULog files
scripts/            Log-analysis utilities
assets/plots/        Figures from verified flight data
```

## Notes

All the hardware and parameters here belong to my own test setups. I am keeping the three drones separate, because a value that works on one frame is not necessarily right for another. I am also keeping the parts that I have not confirmed marked as such, rather than adding guessed specifications.