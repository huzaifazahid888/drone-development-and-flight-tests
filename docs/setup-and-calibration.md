# PX4 setup and calibration

I used QGroundControl for the basic PX4 configuration. My work included setting the correct quadcopter frame, checking motor order and rotation direction, calibrating the RC transmitter, accelerometer, compass and other available sensors, and checking sensor orientation and actuator outputs.

I did not use one set of parameters for all three drones. I have changed frames and hardware during development and I want to keep the saved parameter exports with the drone they belong to.

The initial flights helped me check motor direction, thrust behaviour and the centre of gravity. Later tests moved into GNSS, EKF2, rate and attitude behaviour and analysing the logs after flying.

For any future drone I will record the hardware and software versions, complete calibrations, perform propeller-off motor tests, check failsafe and return modes, and then start with short supervised flight tests.

I will add actual `.params` exports after checking them for details that should not be shared publicly.