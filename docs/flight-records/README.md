# Flight-test records

These pages describe the tests in terms of the aircraft setup, flight mode, purpose, observations and measurements. The raw PX4 recordings are kept separately and are not required to understand the findings.

| Test | Date | Purpose | Main observation |
| --- | --- | --- | --- |
| [Initial Acro control test](initial-acro-test.md) | 4 Nov 2026 | Check gyro vibration and ESC feedback | Vibration near 130–150 Hz and unreliable RPM on two channels |
| [Stabilized control test](stabilized-control-test.md) | 4 Nov 2026 | Examine rate tracking and vibration | Higher roll-band vibration energy than the earlier test |
| [Revised controller test](revised-control-test.md) | 14 Nov 2026 | Review later tuning, power and temperature | About five minutes airborne, battery voltage sag and high reported ESC temperature |

The flights used different modes and configurations, so they should not be treated as a controlled one-variable comparison. See the [controller parameter history](../px4-tuning-history.md) for the recorded settings and the limits of this analysis.

I will add matching video links, verified ranges and more detailed test conditions when available. A [record template](TEMPLATE.md) is included for future flights.
