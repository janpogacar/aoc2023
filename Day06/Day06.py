import re
import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

_, times = lines[0].split(": ")
_, dists = lines[1].split(": ")

time_list = [int(s) for s in re.findall(r'\d+', times)]
dist_list = [int(s) for s in re.findall(r'\d+', dists)]

num_of_results = 1

for i, dist in enumerate(dist_list):
    coeffs = [-1, time_list[i], -1*dist]
    limits = np.roots(coeffs)
    limits = np.sort(limits)

    num_of_results *= ((limits[1] - 1) if limits[1].is_integer() else np.floor(limits[1])) - ((limits[0]+1) if limits[0].is_integer() else np.ceil(limits[0])) +1


print(int(num_of_results))

time2 = ""
dist2 = ""

for i, time in enumerate(time_list):
    time2 += str(time)
    dist2 += str(dist_list[i])

time2 = int(time2)
dist2 = int(dist2)

coeffs = [-1, time2, -1*dist2]
limits = np.roots(coeffs)
limits = np.sort(limits)

num_of_results = ((limits[1] - 1) if limits[1].is_integer() else np.floor(limits[1])) - ((limits[0]+1) if limits[0].is_integer() else np.ceil(limits[0])) +1

print(int(num_of_results))