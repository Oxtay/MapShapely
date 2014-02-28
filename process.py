#!/usr/bin/env python

# This code is to examine the application of Shapely and Fiona for scraping data online and then show them on a map.
# Written by: Okhtay Azarmanesh
# 02/27/2014

# originally inspired by: 
# http://www.macwright.org/2012/10/31/gis-with-python-shapely-fiona.html

import csv
from shapely.geometry import Point, mapping
from fiona import collection

schema = { 'geometry': 'Point', 'properties': { 'name': 'str' } }
with collection(
    "some.shp", "w", "ESRI Shapefile", schema) as output:
    with open('some.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = Point(float(row['lon']), float(row['lat']))
            output.write({
                'properties': {
                    'name': row['name']
                },
                'geometry': mapping(point)
            })