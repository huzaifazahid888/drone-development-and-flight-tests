# PX4 log quick check

This folder has a small Python script that reads a PX4 `.ulg` file with `pyulog` and prints selected battery and ESC results. I can use it as a starting point to check a new flight before writing a separate flight record.

Install dependencies:

```bash
python -m pip install -r scripts/requirements.txt
```

Run:

```bash
python scripts/ulog_quicklook.py path/to/flight.ulg
```

The script prints data only. It does not upload the raw log. The measurements still need to be checked against the actual power module, ESC model and sensor calibration.

The full log may include sensitive position data, so keep raw log files local unless they have been reviewed.