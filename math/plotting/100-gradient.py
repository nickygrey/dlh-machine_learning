#!/usr/bin/env python3
"""Module to plot a scatter plot with a gradient colorbar."""
import matplotlib.pyplot as plt
import numpy as np


def gradient():
    """Plot coordinates colored by elevation with a colorbar."""
    np.random.seed(5)

    x = np.random.randn(2000) * 10
    y = np.random.randn(2000) * 10
    z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))
    plt.figure(figsize=(6.4, 4.8))

    sc = plt.scatter(x, y, c=z)
    cb = plt.colorbar(sc)
    cb.set_label('elevation (m)')
    plt.xlabel('x coordinate (m)')
    plt.ylabel('y coordinate (m)')
    plt.title('Mountain Elevation')
    plt.show()
