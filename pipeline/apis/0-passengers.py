#!/usr/bin/env python3
"""Module to interact with the Star Wars API (SWAPI) to query starships."""
import requests


def availableShips(passengerCount):
    """Retrieve a list of starships that can accommodate passengerCount.

    Args:
        passengerCount (int): Minimum number of passengers required.

    Returns:
        list: Names of available starships.
    """
    url = "https://swapi-api.hbtn.io/api/starships/"
    ships = []

    while url:
        response = requests.get(url).json()
        for ship in response.get('results', []):
            passengers_str = ship.get('passengers', '')
            # Clean string formatting to safely evaluate numbers
            passengers_str = passengers_str.replace(',', '')
            if passengers_str.isdigit():
                if int(passengers_str) >= passengerCount:
                    ships.append(ship.get('name'))
        url = response.get('next')

    return ships
