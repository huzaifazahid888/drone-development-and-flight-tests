# Battery and power

The recent quadcopter uses a Tattu 6S LiPo with a nominal 12000 mAh capacity. I checked the PX4 battery monitor because the useful flight time depends on both actual current consumption and correct sensor calibration.

In the `12_43_50.ulg` log, the battery monitor reported approximately 6639 mAh discharged in about five minutes of flight. It recorded a lowest pack voltage of about 20.35 V and the voltage recovered after the motors stopped. The measurements show substantial voltage sag under load.

The flight parameters included `BAT1_CAPACITY=10800`, `BAT1_R_INTERNAL=0.0025`, `BAT1_V_CHARGED=4.15`, `BAT1_V_EMPTY=3.50`, `BAT1_V_DIV=11.2` and `BAT1_A_PER_V=672`.

These are recorded settings, not recommendations for another drone. I still need to confirm the exact power module and compare the current readings with an independent meter before making final endurance conclusions. The ESC-reported electrical values were not consistent enough to treat as another calibrated power measurement.

I will keep new battery settings and results with the flight in which they were tested.

[Flight record](flight-records/12_43_50.md)