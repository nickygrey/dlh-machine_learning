#!/usr/bin/env python3
"""Module to look up a GitHub user's location or handle rate limits."""
import sys
import time
import requests


def get_user_location():
    """Retrieve and print the location property of a GitHub user profile."""
    if len(sys.argv) < 2:
        return

    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_timestamp = int(response.headers.get('X-Ratelimit-Reset', 0))
        current_timestamp = int(time.time())
        minutes = int(round((reset_timestamp - current_timestamp) / 60))
        print(f"Reset in {minutes} min")
    elif response.status_code == 200:
        user_data = response.json()
        print(user_data.get('location'))


if __name__ == '__main__':
    get_user_location()
