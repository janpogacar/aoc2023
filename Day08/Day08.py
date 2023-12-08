import re
from math import lcm

with open('input.txt') as f:
    lines = f.readlines()

instr = lines[0][:-1]
nodes = []
paths = []


for i in range(2, len(lines)):
    node, rawPath = lines[i].split(" = ")
    nodes.append(node)
    paths.append(rawPath[1:-2].split(", "))

current_node = "AAA"
solution = False
steps = 0
while (solution is False):
    for i, x in enumerate(instr):
        # find list item index
        # find next node
        # move to next node
        # check if node is ZZZ, then break
        steps +=1
        index = nodes.index(current_node)
        if x == "L":
            current_node = paths[index][0]
        elif x == "R":
            current_node = paths[index][1] 
        if current_node == "ZZZ":
            solution = True
            break
        
print(steps)

# Part 2
steps = 0
solution = False
start_nodes = []
for x in nodes:
    if x[-1] == "A":
        start_nodes.append(x)

# get solutions for all starting poins
# find least common multiple
multiples = []

for current_node in start_nodes:
    solution = False
    steps = 0
    while (solution is False):
        for i, x in enumerate(instr):
            # find list item index
            # find next node
            # move to next node
            # check if node is ZZZ, then break
            steps +=1
            index = nodes.index(current_node)
            if x == "L":
                current_node = paths[index][0]
            elif x == "R":
                current_node = paths[index][1] 
            if current_node[-1] == "Z":
                solution = True
                break
    multiples.append(steps)

print(lcm(*multiples))  


