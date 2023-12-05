with open('input.txt') as f:
    lines = f.readlines()

maps = []
end_seed_list = []

# Data parsing
for i, line in enumerate(lines):
    if line.startswith("seeds: "):
        _, seed_string = line.split(": ")
        seed_list = seed_string.split(" ")
    elif "map:" in line:
        k = i+1
        submap = []
        while lines[k] != "\n":
            submap.append(lines[k].split(" "))
            k += 1
        maps.append(submap)

for seed in seed_list: # loop over all seeds
    seed = int(seed)
    for map in maps: # loop over all maps
        for submap in map: # loop over all transformations in a single map
            if seed in range(int(submap[1]), int(submap[1])+int(submap[2])): # check if seed is in range
                seed = seed - int(submap[1]) + int(submap[0])
                break # if correct transformation is found, exit this map to avoid transforming twice

    end_seed_list.append(seed)


# repeat process in reverse for part 2
seed = 0
n = 0
solution = False
while(not solution): # loop until solution is found
    seed = n # start with an incremented value
    for map in maps[::-1]: # Now do transformations in reverse
        for submap in map:
            if seed in range(int(submap[0]), int(submap[0])+int(submap[2])): # Note that because we are transforming in reverse, the range indexes are different
                seed = seed - int(submap[0]) + int(submap[1])
                break

    for i in range(0, len(seed_list), 2): # Check all seed ranges, to see if end result is a valid seed
        if seed in range(int(seed_list[i]), int(seed_list[i])+int(seed_list[i+1])):
            solution = True
            break
    n+=1 # Increment


print(n-1)


print(min(end_seed_list))