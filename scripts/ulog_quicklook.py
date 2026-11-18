#!/usr/bin/env python3
"""Read a few battery and ESC measurements from a PX4 ULog."""

import argparse
from pathlib import Path

import numpy as np
from pyulog import ULog


def get_dataset(log, topic):
    for dataset in log.data_list:
        if dataset.name == topic:
            return dataset.data
    return None


def show_battery(data):
    if data is None:
        print("battery_status was not found")
        return

    print("\nBattery readings")
    fields = (
        ("voltage_v", "Pack voltage", "V"),
        ("current_a", "Current", "A"),
        ("discharged_mah", "Discharged", "mAh"),
        ("remaining", "Remaining", "fraction"),
    )

    for field, label, unit in fields:
        if field not in data:
            continue
        values = np.asarray(data[field], dtype=float)
        values = values[np.isfinite(values)]
        if not values.size:
            continue
        print(f"{label}: min {values.min():.3f}, max {values.max():.3f}, "
              f"last {values[-1]:.3f} {unit}")


def show_esc(data):
    if data is None:
        print("\nesc_status was not found")
        return

    print("\nESC temperature fields")
    found = False
    for field in sorted(data):
        if "temperature" not in field.lower():
            continue
        values = np.asarray(data[field], dtype=float)
        values = values[np.isfinite(values)]
        if not values.size:
            continue
        found = True
        print(f"{field}: median {np.median(values):.1f}, "
              f"max {values.max():.1f}")

    if not found:
        print("No temperature field was available in esc_status")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("log", type=Path)
    args = parser.parse_args()

    log = ULog(str(args.log))
    print(f"File: {args.log.name}")
    print(f"Logged topics: {len(log.data_list)}")

    show_battery(get_dataset(log, "battery_status"))
    show_esc(get_dataset(log, "esc_status"))

    print("\nThese are onboard readings, not independently verified values.")


if __name__ == "__main__":
    main()
