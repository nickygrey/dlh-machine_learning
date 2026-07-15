#!/usr/bin/env python3
"""Module to fetch and display the first upcoming SpaceX launch."""
import requests


def fetch_first_launch():
    """Fetch the earliest upcoming SpaceX launch and print its details."""
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    response = requests.get(url).json()

    if not response:
        return

    # Sort upcoming launches by date_unix ascending
    response.sort(key=lambda x: x.get('date_unix', 0))
    first_launch = response[0]

    launch_name = first_launch.get('name')
    date_local = first_launch.get('date_local')
    rocket_id = first_launch.get('rocket')
    launchpad_id = first_launch.get('launchpad')

    # Fetch rocket name details
    rocket_base = "https://api.spacexdata.com/v4/rockets/"
    rocket_url = f"{rocket_base}{rocket_id}"
    rocket_name = requests.get(rocket_url).json().get('name')

    # Fetch launchpad locale details
    launchpad_base = "https://api.spacexdata.com/v4/launchpads/"
    launchpad_url = f"{launchpad_base}{launchpad_id}"
    launchpad_res = requests.get(launchpad_url).json()
    launchpad_name = launchpad_res.get('name')
    launchpad_locality = launchpad_res.get('locality')

    # Print the formatted metadata
    print(f"{launch_name} ({date_local}) {rocket_name} - "
          f"{launchpad_name} ({launchpad_locality})")


if __name__ == '__main__':
    fetch_first_launch()
