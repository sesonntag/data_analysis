#!/usr/bin/env python
#
# ******************************************************************************
# Title: analyze_auger_data.py
# Description: Read Auger public data and analyze accordingly
# Author: Sebastian Sonntag
# Date: 2019-12-29
# License:
# ******************************************************************************

import pandas as pd

df = pd.read_csv('auger_public_2019_12_29.txt', sep=' ', skiprows=19,
                 names=['event_id', 'n_stations', 'angle_theta', 'angle_phi',
                        'energy', 'unix_time', 'galactic_longitude',
                        'galactic_latitude'])
print(df.head())
