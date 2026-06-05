#!/usr/bin/env python3
"""Module to plot a mathematical line graph."""
import matplotlib.pyplot as plt
import numpy as np


def line():
    """Plot y as a solid red line with a defined x-axis range."""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    plt.plot(y, 'r')
    plt.xlim(0, 10)
    plt.show()
