# GNSS and EKF2

I spent some time understanding the effect of GNSS antenna position on the state estimator. The flight controller and GNSS antenna are not always at the centre of gravity. When the drone rotates, an antenna away from the reference point moves in space even if the reference point has no translational movement.

The GNSS measures position and velocity at its antenna. EKF2 can account for the lever-arm offset when the position of the antenna relative to the vehicle body is configured correctly. The offset is not a GPS rotation measurement. It helps the estimator relate the antenna measurements to the correct vehicle reference.

In my setup I measured about 20 cm horizontal separation from the flight controller and about 5 cm vertical separation. I still need the signed directions in the PX4 body axes and the actual centre-of-gravity reference before publishing final parameters.

I also checked how a heavy battery mounted below the flight controller can move the centre of gravity downward. A visually central flight controller is not automatically at the vehicle's centre of gravity.

I will add the final sensor offsets and the matching hardware photo after confirming the mounting.