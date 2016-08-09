# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:57:05 2016

@author: jack

NOTES
=====
This is a script to plot data from a gpx file on a map 
<https://ocefpaf.github.io/python4oceanographers/blog/2014/08/18/gpx/>
"""


import gpxpy

# open file
filename = '/home/jack/Documents/Environments/map/runkeeper-data/2016-08-04-0730.gpx'
gpx = gpxpy.parse(open(filename))


print("{} track(s)".format(len(gpx.tracks)))
track = gpx.tracks[0]

print("{} segment(s)".format(len(track.segments)))
segment = track.segments[0]

print("{} point(s)".format(len(segment.points)))
points = segment.points


#%%
# use a for loop with enumerate and append to loop through all tracks and segments
data = []
segment_length = segment.length_3d()
for point_idx, point in enumerate(segment.points):
    data.append([point.longitude, point.latitude,
                 point.elevation, point.time, segment.get_speed(point_idx)])


long = data[:,0]
lat = data[:,1]
plt.plot(long,lat,linewidth=4.0)
mplleaflet.show()

# display a table
# pandas is a package for working with data.  its probably more complicated than I need.
from pandas import DataFrame

columns = ['Longitude', 'Latitude', 'Altitude', 'Time', 'Speed']
df = DataFrame(data, columns=columns)
df.head()



#%%

import numpy as np
import seawater as sw
from oceans.ff_tools import smoo1

_, angles = sw.dist(df['Latitude'], df['Longitude'])
angles = np.r_[0, np.deg2rad(angles)]

# Normalize the speed to use as the length of the arrows
r = df['Speed'] / df['Speed'].max()
kw = dict(window_len=31, window='hanning')
df['u'] = smoo1(r * np.cos(angles), **kw)
df['v'] = smoo1(r * np.sin(angles), **kw)


#%%
import mplleaflet
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
df = df.dropna()
ax.plot(df['Longitude'], df['Latitude'],
        color='darkorange', linewidth=5, alpha=0.5)
sub = 10
ax.quiver(df['Longitude'][::sub], df['Latitude'][::sub], df['u'][::sub], df['v'][::sub], color='deepskyblue', alpha=0.8, scale=10)
mplleaflet.display(fig=fig, tiles='esri_aerial')



