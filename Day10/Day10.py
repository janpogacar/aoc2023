from copy import deepcopy

with open('input.txt') as f:
    lines = f.readlines()

maze = []

for x in lines:
    maze.append(list(x)[:-1])

maze2 = deepcopy(maze)

# manually code these values
pos_x = 110
pos_y = 41
dir = "l" # Left Right Up Down

#pos_x = 4
#pos_y = 1
#dir = "d" # Left Right Up Down


dist = 1
pipe_list = []
#maze2[pos_y][pos_x] = "*"
pipe_list.append([pos_y, pos_x])

while(True):
    if maze[pos_y][pos_x] == "S":
        break
    if dir == "r":
        if maze[pos_y][pos_x] == "-":
            pos_x +=1
        elif maze[pos_y][pos_x] == "J":
            pos_y -= 1
            dir = "u"
        elif maze[pos_y][pos_x] == "7":
            pos_y += 1
            dir = "d"
    elif dir == "l":
        if maze[pos_y][pos_x] == "-":
           pos_x -=1
        elif maze[pos_y][pos_x] == "L":
            pos_y -= 1
            dir = "u"
        elif maze[pos_y][pos_x] == "F":
            pos_y += 1
            dir = "d"
    elif dir == "u":
        if maze[pos_y][pos_x] == "|":
            pos_y -= 1
        elif maze[pos_y][pos_x] == "7":
            pos_x -= 1
            dir = "l"
        elif maze[pos_y][pos_x] == "F":
            pos_x += 1
            dir = "r"
    elif dir == "d":
        if maze[pos_y][pos_x] == "|":
            pos_y += 1
        elif maze[pos_y][pos_x] == "J":
            pos_x -= 1
            dir = "l"
        elif maze[pos_y][pos_x] == "L":
            pos_x += 1
            dir = "r"
    dist += 1
    #maze2[pos_y][pos_x] = "*"
    pipe_list.append([pos_y, pos_x])

for i in range(len(maze2)):
    for j in range(len(maze2[0])):
        if [i,j] not in pipe_list:
          maze2[i][j] = "." 

result2 = 0

for line in maze2:
    inside = False
    for x in line:
        if inside and x == ".":
            result2 += 1
        if x in ["|", "J", "L", "S"]: # S is J in my case, so this is hardcoded
            inside = not inside

            
print(dist/2)
print(result2)