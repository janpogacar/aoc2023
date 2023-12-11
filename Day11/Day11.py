import numpy as np
from copy import deepcopy
from itertools import combinations
from scipy.spatial.distance import cityblock

np.seterr(all='warn')

with open('input.txt') as f:
    lines = f.readlines()

map = []

for x in lines:
    map.append(list(x)[:-1])

map2 = deepcopy(map)
map_pt2 = deepcopy(map)
k = 0
for i, line in enumerate(map2):
    if set(line) == {'.'}:
        map.insert(i+k, line)
        k+=1
    
map = np.transpose(map)
map2 = deepcopy(map)

k=0
for i, line in enumerate(map2):
    if set(line) == {'.'}:
        map = np.insert(map, i+k, line, axis = 0)
        k+=1

map = np.transpose(map)


stars = []

for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == "#":
            stars.append([y, x])

pairs = list(combinations(stars, 2))

path_len = 0

for x in pairs:
    path_len += cityblock(x[0], x[1])

print(path_len)
stars2 = []
# part 2
# map the points first
for y in range(len(map_pt2)):
    for x in range(len(map_pt2[0])):
        if map_pt2[y][x] == "#":
            stars2.append([y, x])

stars2_cpy = deepcopy(stars2)

for i, line in enumerate(map_pt2):
    if set(line) == {'.'}:
        #increase all y indices of stars by N
        for j, star in enumerate(stars2):
            if star[0] > i:
                stars2_cpy[j][0] += 1000000-1

map_pt2 = np.transpose(map_pt2)

for i, line in enumerate(map_pt2):
    if set(line) == {'.'}:
        #increase all x indices of stars by N
        for j, star in enumerate(stars2):
            if star[1] > i:
                stars2_cpy[j][1] += 1000000-1


pairs = list(combinations(stars2_cpy, 2))

path_len2 = np.uint64(0)

for x in pairs:
    path_len2 += cityblock(x[0], x[1])

print(path_len2)
