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
# response = requests.get("http://api.open-notify.org/astros.json")
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


# tester = haversine(bp_lon, bp_lat, 5, 50)
# print(tester)

# inverse haversine function
# def havers_inv()

from math import asin, atan2, cos, degrees, radians, sin

def get_point_at_distance(lat1, lon1, d, bearing, R=6378.137):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    a = radians(bearing)
    lat2 = asin(sin(lat1) * cos(d/R) + cos(lat1) * sin(d/R) * cos(a))
    lon2 = lon1 + atan2(
        sin(a) * sin(d/R) * cos(lat1),
        cos(d/R) - sin(lat1) * sin(lat2)
    )
    return (degrees(lat2), degrees(lon2))

def get_point_at_dist_str(lat1, lon1, d, bearing, R=6378.137):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    a = radians(bearing)
    lat2 = asin(sin(lat1) * cos(d/R) + cos(lat1) * sin(d/R) * cos(a))
    lon2 = lon1 + atan2(
        sin(a) * sin(d/R) * cos(lat1),
        cos(d/R) - sin(lat1) * sin(lat2)
    )
    lat_2 = degrees(lat2)
    lon_2 = degrees(lon2)
    lat2_lon2 = str(lat_2) +"," + str(lon_2)
    return lat2_lon2

lat = 50.85217062538557
lon = 5.6906075839614285

# radius
inp_dist = 10.0
#rad_c1 = inp_dist / (2 + np.sqrt(2))
rad_c = inp_dist / 3.5

# circle points, 25 points, 1 origin, 12 on 90 degree lines, 12 inside the quarter circles
# origin lat,lon in string format
lat_o = 50.85217062538557
lon_o = 5.6906075839614285
origin = str(lat_o) + "," + str(lon_o)
print(origin)

# 12 points along axis from origin
# distance parameters
adj_rad_1 = 0.67 * rad_c
adj_rad_2 = 0.33 * rad_c

# 3 points at 0 degrees (up):
u1 = get_point_at_dist_str(lat_o, lon_o, rad_c, 0)
u2 = get_point_at_dist_str(lat_o, lon_o, adj_rad_1, 0)
u3 = get_point_at_dist_str(lat_o, lon_o, adj_rad_2, 0)

# 3 points at 90 degrees (right):
r1 = get_point_at_dist_str(lat_o, lon_o, rad_c, 90)
r2 = get_point_at_dist_str(lat_o, lon_o, adj_rad_1, 90)
r3 = get_point_at_dist_str(lat_o, lon_o, adj_rad_2, 90)

# 3 points at 180 degrees (down):
d1 = get_point_at_dist_str(lat_o, lon_o, rad_c, 180)
d2 = get_point_at_dist_str(lat_o, lon_o, adj_rad_1, 180)
d3 = get_point_at_dist_str(lat_o, lon_o, adj_rad_2, 180)

# 3 points at 270 degrees (left):
l1 = get_point_at_dist_str(lat_o, lon_o, rad_c, 270)
l2 = get_point_at_dist_str(lat_o, lon_o, adj_rad_1, 270)
l3 = get_point_at_dist_str(lat_o, lon_o, adj_rad_2, 270)

# 4 points on smaller inner circle at 45, 135, etc. degrees
# distance parameters
adj_rad_3 = 0.5 * rad_c
# 1 point at 45 degrees (up, right)
ur1 = get_point_at_dist_str(lat_o, lon_o, adj_rad_3, 45)
# 1 point at 135 degrees (right, down)
dr2 = get_point_at_dist_str(lat_o, lon_o, adj_rad_3, 135)
# 1 point at 225 degrees (down, left)
dl3 = get_point_at_dist_str(lat_o, lon_o, adj_rad_3, 225)
# 1 point at 315 degrees (left, up)
ul4 = get_point_at_dist_str(lat_o, lon_o, adj_rad_3, 315)

# 8 points on bigger inner circle at 30, 60, 120, 150, etc. degrees
# distance parameters
adj_rad_4 = 0.83 * rad_c
# 2 points at 30, 60 degrees (up, right)
uur1 = get_point_at_dist_str(lat_o, lon_o, adj_rad_4, 30)
urr2 = get_point_at_dist_str(lat_o, lon_o, adj_rad_4, 60)
# 2 points at 120, 150 degrees (down, right)
drr1 = get_point_at_dist_str(lat_o, lon_o, adj_rad_4, 120)
ddr2 = get_point_at_dist_str(lat_o, lon_o, adj_rad_4, 150)
# 2 points at 210, 240 degrees (down, left)
ddl1 = get_point_at_dist_str(lat_o, lon_o, adj_rad_4, 210)
dll2 = get_point_at_dist_str(lat_o, lon_o, adj_rad_4, 240)
# 2 points at 300, 330 degrees (up, left)
ull1 = get_point_at_dist_str(lat_o, lon_o, adj_rad_4, 300)
uul2 = get_point_at_dist_str(lat_o, lon_o, adj_rad_4, 330)

# combine all points in one string to use in destination and origins for google api
# now for testing, origin is only the origin, destinations is the 24 other points
origin_points = origin + "|" + ur1 + "|" + dr2 + "|" + dl3 + "|" + ul4

circle_points = (u1 + "|" + u2 + "|" + u3 + "|" + r1 + "|" + r2 + "|" + r3 + "|"
                 + d1 + "|" + d2 + "|" + d3 + "|" + l1 + "|" + l2 + "|" + l3 + "|"
                 + uur1 + "|" + urr2 + "|" + drr1 + "|" + ddr2 + "|" + ddl1 + "|"
                 + dll2 + "|" + ull1 + "|" + uul2)


# for 25 x 25, exceeds the 100 limits
# circle_points = (origin + "|" + u1 + "|" + u2 + "|" + u3 + "|" + r1 + "|" + r2 + "|" + r3 + "|"
#                  + d1 + "|" + d2 + "|" + d3 + "|" + l1 + "|" + l2 + "|" + l3 + "|"
#                  + ur1 + "|" + dr2 + "|" + dl3 + "|" + ul4 + "|" + uur1 + "|" + urr2 + "|"
#                  + drr1 + "|" + ddr2 + "|" + ddl1 + "|" + dll2 + "|" + ull1 + "|" + uul2)
print(origin_points)
print(circle_points)

"""

# API part
# read google api from txt key
api_file = open("api_key.txt", "r")
api_key = api_file.readline()
api_file.close()

# base url https://maps.googleapis.com/maps/api/distancematrix/outputFormat?parameters
# for now using coordinates, place ID is more efficient
# perhaps later implement a way to get place ID from given coordinates
url = "https://maps.googleapis.com/maps/api/distancematrix/json?"

# get response
r = requests.get(url + "destinations=" + origin_points + "&origins=" + circle_points + "&mode=walking" + "&units=metric" + "&key=" + api_key)
print(r.json())

# distance matrix to fill, 5 x 20
row_test_txt = r.json()["rows"][0]["elements"][0]["distance"]["text"]
row_test_meter = r.json()["rows"][0]["elements"][0]["distance"]["value"]

print(row_test_txt)
print(row_test_meter)

# destination addresses
dest_address = r.json()["destination_addresses"]
num_dest = len(dest_address)
# origin addresses
orig_address = r.json()["origin_addresses"]
num_orig = len(orig_address)

# array to fill with arrays
dist_mat = []

for i in range(0, num_orig):
    temp_row = []
    for j in range(0, num_dest):
        temp_row.append(r.json()["rows"][i]["elements"][j]["distance"]["value"])
    dist_mat.append(temp_row)

print(dist_mat)
"""

dist_mat_prime = [[4744, 3278, 5545, 6307, 5650],
                  [2490, 3919, 4293, 4130, 2876],
                  [991, 2442, 2794, 2631, 1587],
                  [3469, 3418, 2491, 4575, 5063],
                  [2296, 2334, 1675, 3486, 3979],
                  [1319, 1760, 1383, 2719, 3224],
                  [3219, 4768, 2931, 2792, 4685],
                  [2211, 3896, 2060, 1642, 3535],
                  [1072, 2796, 1452, 1150, 2619],
                  [3625, 5007, 5201, 2853, 2617],
                  [2329, 3831, 3905, 1557, 1628],
                  [1432, 3081, 3008, 1480, 1445],
                  [3184, 1423, 3984, 4746, 4089],
                  [3375, 1742, 2888, 4591, 3951],
                  [3018, 3599, 1834, 3919, 4774],
                  [2916, 3908, 1395, 3166, 4519],
                  [2736, 4549, 2998, 1385, 3500],
                  [2783, 4698, 3949, 1466, 2867],
                  [3037, 4122, 4823, 2754, 1244],
                  [2883, 3801, 4687, 3290, 1228]]

# parameters for determining subsets of points, 16 total
# list with all point names
point_list = [u1, u2, u3, r1, r2, r3, d1, d2, d3, l1, l2, l3, uur1, urr2, drr1, ddr2, ddl1, dll2, ull1, uul2, origin, ur1, dr2, dl3, ul4]
point_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
               20, 21, 22, 23, 24]

# subset indexes
# four quadrants
plane1 = [[0, 1, 2, 3, 4, 5, 12, 13], [0, 1]]
plane2 = [[3, 4, 5, 6, 7, 8, 14, 15], [0, 2]]
plane3 = [[6, 7, 8, 9, 10, 11, 16, 17], [0, 3]]
plane4 = [[0, 1, 2, 9, 10, 11, 18, 19], [0, 4]]
# subset types 2, upper half circle (5), bottom half circle (6)
upper_hc = [[0, 1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 18, 19], [0, 1, 4]]
lower_hc = [[0, 1, 2, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17], [0, 2, 3]]
# subset types 2, left half circle (7), right half circle (8)
left_hc = [[0, 1, 2, 6, 7, 8, 9, 10, 11, 16, 17, 18, 19], [0, 3, 4]]
right_hc = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 14, 15], [0, 1, 2]]
# subset type 3, horizontal middle cut
horizon_mc = [[2, 3, 4, 5, 8, 9, 10, 11, 13, 14, 17, 18], [0, 1, 2, 3, 4]]
# subset type 3, vertical middle cut
vertical_mc = [[0, 1, 2, 5, 6, 7, 8, 11, 12, 15, 16, 19], [0, 1, 2, 3, 4]]
# subset type 4, major diagonal (\) cut left and right
left_mad = [[6, 7, 8, 9, 10, 11, 15, 16, 17, 18], [0, 2, 3, 4]]
right_mad = [[0, 1, 2, 3, 4, 5, 12, 13, 14, 19], [0, 1, 2, 4]]
# subset type 5, minor diagnoal (/) cut left and right
left_mid = [[0, 1, 2, 9, 10, 11, 12, 17, 18, 19], [0, 1, 3, 4]]
right_mid = [[3, 4, 5, 6, 7, 8, 13, 14, 15, 16], [0, 1, 2, 3]]

# sum of distances per "cut"
# four quadrants
pl1_sum = 0
pl2_sum = 0
pl3_sum = 0
pl4_sum = 0
for x in range(0, 7):
    for y in range(0, 1):
        # change to dist_mat instead of dist_mat_prime when using API
        pl1_sum += dist_mat_prime[plane1[0][x]][plane1[1][y]]
        pl2_sum += dist_mat_prime[plane2[0][x]][plane2[1][y]]
        pl3_sum += dist_mat_prime[plane3[0][x]][plane3[1][y]]
        pl4_sum += dist_mat_prime[plane4[0][x]][plane4[1][y]]

# subset types 2, upper half circle (5), bottom half circle (6)
uphc_sum = 0
lowhc_sum = 0
for x in range(0, len(upper_hc[0])):
    for y in range(0, len(upper_hc[1])):
        uphc_sum += dist_mat_prime[upper_hc[0][x]][upper_hc[1][y]]
        lowhc_sum += dist_mat_prime[lower_hc[0][x]][lower_hc[1][y]]

# subset types 2, left half circle (7), right half circle (8)
lefthc_sum = 0
righthc_sum = 0
for x in range(0, len(left_hc[0])):
    for y in range(0, len(left_hc[1])):
        lefthc_sum += dist_mat_prime[left_hc[0][x]][left_hc[1][y]]
        righthc_sum += dist_mat_prime[right_hc[0][x]][right_hc[1][y]]

# subset type 3, horizontal middle cut
hormc_sum = 0
for x in range(0, len(horizon_mc[0])):
    for y in range(0, len(horizon_mc[1])):
        hormc_sum += dist_mat_prime[horizon_mc[0][x]][horizon_mc[1][y]]
# subset type 3, vertical middle cut
vermc_sum = 0
for x in range(0, len(vertical_mc[0])):
    for y in range(0, len(vertical_mc[1])):
        vermc_sum += dist_mat_prime[vertical_mc[0][x]][vertical_mc[1][y]]

# subset type 4, major diagonal (\) cut left and right
leftmad_sum = 0
rightmad_sum = 0
for x in range(0, len(left_mad[0])):
    for y in range(0, len(left_mad[1])):
        leftmad_sum += dist_mat_prime[left_mad[0][x]][left_mad[1][y]]
        rightmad_sum += dist_mat_prime[right_mad[0][x]][right_mad[1][y]]

# subset type 5, minor diagnoal (/) cut left and right
leftmid_sum = 0
rightmid_sum = 0
for x in range(0, len(left_mid[0])):
    for y in range(0, len(left_mid[1])):
        leftmid_sum += dist_mat_prime[left_mid[0][x]][left_mid[1][y]]
        rightmid_sum += dist_mat_prime[right_mid[0][x]][right_mid[1][y]]


# paste of subset names:
# four quadrants
# plane one lengths:
plane_x, plane_y = len(plane1[0]), len(plane1[1])
plane_xy = plane_x * plane_y
print("planex sums:", pl1_sum, pl2_sum, pl3_sum, pl4_sum)
print("planex sums/points product", pl1_sum/plane_xy, pl2_sum/plane_xy, pl3_sum/plane_xy, pl4_sum/plane_xy)
print("planex lengths:", plane_x, plane_y)
# subset types 2, upper half circle (5), bottom half circle (6)
upper_hc_x, upper_hc_y = len(upper_hc[0]), len(upper_hc[1])
upper_hc_xy = upper_hc_x * upper_hc_y
print("upper, bottom half circle sums:", uphc_sum, lowhc_sum)
print("upper, bottom half circle sums/points product:", uphc_sum/upper_hc_xy, lowhc_sum/upper_hc_xy)
print("upper, bottom half circle lengths:", upper_hc_x, upper_hc_y)
# subset types 2, left half circle (7), right half circle (8)
left_hc_x, left_hc_y = len(left_hc[0]), len(left_hc[1])
left_hc_xy = left_hc_x * left_hc_y
print("left, right half circle sums:", lefthc_sum, righthc_sum)
print("left, right half circle sums/points product:", lefthc_sum/left_hc_xy, righthc_sum/left_hc_xy)
print("left, right half circle lengths:", left_hc_x, left_hc_y)
# subset type 3, horizontal middle cut
horizon_mc_x, horizon_mc_y = len(horizon_mc[0]), len(horizon_mc[1])
horizon_mc_xy = horizon_mc_x * horizon_mc_y
print("horizontal middle cut sum:", hormc_sum)
print("horizontal middle cut sum/points product:", hormc_sum/horizon_mc_xy)
print("horizontal middle cut length:", horizon_mc_x, horizon_mc_y)
# subset type 3, vertical middle cut
vertical_mc_x, vertical_mc_y = len(vertical_mc[0]), len(vertical_mc[1])
vertical_mc_xy = vertical_mc_x * vertical_mc_y
print("vertical middle cut sum:", vermc_sum)
print("vertical middle cut sum/points product:", vermc_sum/vertical_mc_xy)
print("vertical middle cut length:", vertical_mc_x, vertical_mc_y)
# subset type 4, major diagonal (\) cut left and right
left_mad_x, left_mad_y = len(left_mad[0]), len(left_mad[1])
left_mad_xy = left_mad_x * left_mad_y
print("major diagonal cuts left right sums:", leftmad_sum, rightmad_sum)
print("major diagonal cuts left right sums/points product:", leftmad_sum/left_mad_xy, rightmad_sum/left_mad_xy)
print("major diagonal cuts length:", left_mad_x, left_mad_y)
# subset type 5, minor diagnoal (/) cut left and right
left_mid_x, left_mid_y = len(left_mid[0]), len(left_mid[1])
left_mid_xy = left_mid_x * left_mid_y
print("major diagonal cuts left right sums:", leftmid_sum, rightmid_sum)
print("major diagonal cuts left right sums/points product:", leftmid_sum/left_mid_xy, rightmid_sum/left_mid_xy)
print("major diagonal cuts length:", left_mid_x, left_mid_y)
