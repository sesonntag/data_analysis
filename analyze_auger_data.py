#!/usr/bin/env python
#
# ******************************************************************************
# Title: analyze_auger_data.py
# Description: Read Auger public data and analyze accordingly
# Author: Sebastian Sonntag
# Date: 2020-12-29
# License:
# ******************************************************************************

import pandas as pd
# from datetime import datetime
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# define a fit function
def func(x, m, b):
    return m * x + b


# import the data and cast types
df = pd.read_csv('auger_public_2019_12_29.txt', sep=' ', skiprows=19,
                 names=['event_id', 'n_stations', 'angle_theta', 'angle_phi',
                        'energy', 'unix_time', 'galactic_longitude',
                        'galactic_latitude'])
df['cet_time'] = pd.to_datetime(df['unix_time'], unit='s')

# define common filter on the data
df_filtered = df[(df['energy'] >= 10)]

# do the actual fit
popt, pcov = curve_fit(func, df_filtered['angle_theta'], df_filtered['energy'])

# plot the results
plt.scatter(df_filtered['angle_theta'], df_filtered['energy'],
            c=df_filtered['n_stations'])
plt.plot(df_filtered['angle_theta'], func(df_filtered['angle_theta'], *popt),
         'r-', label='fit: m=%5.3f, b=%5.3f,' % tuple(popt))
plt.colorbar()
plt.xlabel('Angle (theta) of incidence / °')
plt.ylabel('Energy / Eev')
plt.title('Plot')
plt.legend()
plt.show()
