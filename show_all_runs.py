# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:57:05 2016

@author: jack

NOTES
=====
This is modified from code I got here:
<https://ocefpaf.github.io/python4oceanographers/blog/2014/08/18/gpx/>

TO DO
=====
Some changes I'd like to make:
-fix the problem where it doesn't show some of my runs
-add ability to only show points in Muroran
-change plotting settins to make points larger, or to make continuous lines 
that don't connect endpoints
"""


import gpxpy
import os
import numpy as np
from matplotlib import pyplot as plt
import mplleaflet

gpxFiles = []
entireFolder = os.listdir('/home/jack/Documents/Environments/map/' +
                          'runkeeper-data')
for i in range(len(entireFolder)):
    if entireFolder[i][-3:] == 'gpx':
        gpxFiles.append(entireFolder[i])

long = []
lat = []
for i in range(len(gpxFiles[2:])):
    # open file
    filename = ('/home/jack/Documents/Environments/map/runkeeper-data/' +
                gpxFiles[i])
    print(filename)
    gpx = gpxpy.parse(open(filename))
    
    track = gpx.tracks[0]
    segment = track.segments[0]
    segment_length = segment.length_3d()
    for point_idx, point in enumerate(segment.points):
        long.append(point.longitude)
        lat.append(point.latitude)
        len(np.array(long[:]*1))

    #plt.figure()    
    #plt.plot(long,lat,linewidth=4.0)


plt.figure()    
plt.plot(long,lat,'x')
set_markersize(8)
mplleaflet.show()






