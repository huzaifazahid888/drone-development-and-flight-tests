# Hardware

My work has passed through three quadcopter sizes: a small drone, a mid-size drone and the current 736 × 615 mm drone. I am keeping their hardware information separate because I have changed the physical setup during development.

The recent PX4 log identifies the flight controller as `PX4_FMU_V6X`, subtype `V6X008`. This describes the firmware board family, not the manufacturer printed on the hardware.

The recent large-drone setup uses a Tattu 6S 12000 mAh LiPo battery and four ESC channels are visible in the log. I still need to confirm the exact ESC, motor, propeller and power module models before publishing a final bill of materials.

During GNSS setup I measured the antenna as approximately 20 cm from the flight-controller reference and 5 cm higher. I still need to confirm which direction those offsets have in the controller axes before publishing them as final EKF2 parameters.

The sight/camera and telemetry share one RF transmission link. I have observed intermittent video interruptions and will add the exact RF and camera models after checking them.

[Small drone](../vehicles/01-small-drone/README.md) · [Mid-size drone](../vehicles/02-mid-size-drone/README.md) · [Large drone](../vehicles/03-large-drone/README.md)