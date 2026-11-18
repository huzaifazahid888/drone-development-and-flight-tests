# Video and telemetry over RF

The current quadcopter has a sight/camera that continuously sends live video to the ground station. MAVLink telemetry and video use the same RF link.

During testing I noticed that the video is sometimes lost or interrupted instead of arriving continuously. I have not yet confirmed whether the interruption comes from RF packet loss, bandwidth, encoder or decoder buffering, or the power supply.

My next check is whether telemetry stays connected at the moment the video freezes. I will also look at the video resolution and bitrate, RF signal information, the camera-to-RF interface and the supply voltage of the sight and transmitter.

I do not want to reduce essential flight telemetry or change PX4 parameters without first checking whether the telemetry stream is really causing congestion. Video usually needs much more bandwidth than MAVLink, but the real link capacity and both stream rates need measurement.

The RF and camera model numbers, ground-station setup and matching video example will be added later. The issue is not marked as solved.