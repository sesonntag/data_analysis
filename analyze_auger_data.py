#!/usr/bin/env python
#
# ******************************************************************************
# Title: analyze_auger_data.py
# Description: Read Auger public data and analyze accordingly
# Author: Sebastian Sonntag
# Date: 2020-01-02
# License:
# ******************************************************************************

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('auger_public_2019_12_29.txt', sep=' ', skiprows=19,
                 names=['event_id', 'n_stations', 'angle_theta', 'angle_phi',
                        'energy', 'unix_time', 'galactic_longitude',
                        'galactic_latitude'])

df['cet_time'] = pd.to_datetime(df['unix_time'], unit='s')

#plt.scatter(df['angle_phi'], df['angle_theta'])
plt.hist(df['angle_theta'], bins=20)
plt.show()
