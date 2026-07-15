#!/usr/bin/env python3
"""Module to calculate and display the launch frequency of SpaceX rockets."""
import requests


def get_rocket_frequency():
    """Retrieve and print launch counts per rocket, sorted correctly."""
    rockets_url = "https://api.spacexdata.com/v4/rockets"
    launches_url = "https://api.spacexdata.com/v4/launches"

    try:
        rockets_resp = requests.get(rockets_url).json()
        launches_resp = requests.get(launches_url).json()
    except Exception:
        return

    # Map rocket IDs to their names
    rocket_map = {r.get('id'): r.get('name') for r in rockets_resp}

    # Count launches per rocket name
    frequency = {}
    for launch in launches_resp:
        rocket_id = launch.get('rocket')
        if rocket_id:
            rocket_name = rocket_map.get(rocket_id)
            if rocket_name:
                frequency[rocket_name] = frequency.get(rocket_name, 0) + 1

    # Sort: Descending by launch count, then alphabetically ascending
    sorted_rockets = sorted(
        frequency.items(),
        key=lambda x: (-x[1], x[0])
    )

    for name, count in sorted_rockets:
        print(f"{name}: {count}")


if __name__ == '__main__':
    get_rocket_frequency()
