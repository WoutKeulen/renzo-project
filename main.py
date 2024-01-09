# Test script for route project

# import statements
import numpy as np
import requests
import json
import smtplib

# parameters for testing
dd_lat = 50.85217062538557
dd_lon = 5.6906075839614285
gbw_lat = 50.853240330604926
gbw_lon = 5.868641185506192
bp_lat = 50.86125729307938
bp_lon = 5.834178815299351

# api test code, uses free api to test connection
response = requests.get("http://api.open-notify.org/astros.json")
# print(response.status_code)
# print(response.json())

def jprint(obj):
    # create a formatted string of Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# jprint(response.json())

# haversine function
def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    lon_dif = lon2 - lon1
    lat_dif = lat2 - lat1
    a = np.sin(lat_dif / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(lon_dif / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6378.137
    return c * r


tester = haversine(bp_lon, bp_lat, 5, 50)
print(tester)

# inverse haversine function
# def havers_inv()

from math import asin, atan2, cos, degrees, radians, sin

def get_point_at_distance(lat1, lon1, d, bearing, R=6378.137):
    """
    lat: initial latitude, in degrees
    lon: initial longitude, in degrees
    d: target distance from initial
    bearing: (true) heading in degrees
    R: optional radius of sphere, defaults to mean radius of earth

    Returns new lat/lon coordinate {d}km from initial, in degrees
    """
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    a = radians(bearing)
    lat2 = asin(sin(lat1) * cos(d/R) + cos(lat1) * sin(d/R) * cos(a))
    lon2 = lon1 + atan2(
        sin(a) * sin(d/R) * cos(lat1),
        cos(d/R) - sin(lat1) * sin(lat2)
    )
    return (degrees(lat2), degrees(lon2),)

lat = 50.85217062538557
lon = 5.6906075839614285
distance = 5
bearing1 = 90
bearing2 = 180
bearing3 = 270
bearing4 = 0
lat2_90, lon2_90 = get_point_at_distance(lat, lon, distance, bearing1)
lat2_180, lon2_180 = get_point_at_distance(lat, lon, distance, bearing2)
lat2_270, lon2_270 = get_point_at_distance(lat, lon, distance, bearing3)
lat2_0, lon2_0 = get_point_at_distance(lat, lon, distance, bearing4)

print(lat2_90, lon2_90)
print(lat2_180, lon2_180)
print(lat2_270, lon2_270)
print(lat2_0, lon2_0)



# google api
api_file = open("api_key.txt", "r")
api_key = api_file.readline()
api_file.close()

# starting point input
st_point_lat, st_point_lon = 50.85217062538557, 5.6906075839614285

# end point input
# end_point_lat, end_point_lon = 50.85217062538557, 5.6906075839614285
