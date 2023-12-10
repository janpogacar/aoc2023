from copy import deepcopy

queue = []     #Initialize a queue
def maze_bfs(pos_y, pos_x): #function for BFS
  queue.append([pos_y, pos_x])

  while queue:          # Creating loop to visit each node
    y, x = queue.pop(0)
    if x == 75 and y == 75:
        print(0) 
    #print (m, end = " ") 
    if (x+1) in range(0, len(maze2[0])) and maze2[y][x+1] != "*":
       maze2[y][x+1] = "*"
       queue.append([y, x+1])
    if (x-1) in range(0, len(maze2[0])) and maze2[y][x-1] != "*":
       maze2[y][x-1] = "*"
       queue.append([y, x-1])
    if (y+1) in range(0, len(maze2)) and maze2[y+1][x] != "*":
       maze2[y+1][x] = "*"
       queue.append([y+1, x])
    if (y-1) in range(0, len(maze2)) and maze2[y-1][x] != "*":
       maze2[y-1][x] = "*"
       queue.append([y-1, x])

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
maze2[pos_y][pos_x] = "*"

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
    maze2[pos_y][pos_x] = "*"

f = open('debug.txt', 'w')
for i in maze2:
    tmp = ""
    for j in i:
        tmp += j
    f.write(tmp + '\n')

for i in range(len(maze2)):
    for j in range(len(maze2[0])):
        if maze2[i][j] != "*":
          maze2[i][j] = "." 

f = open('debug2.txt', 'w')
for i in maze2:
    tmp = ""
    for j in i:
        tmp += j
    f.write(tmp + '\n')

# run bfs for all edges
for x in range(0, len(maze2[0])):
    maze_bfs(0, x)
    maze_bfs(len(maze2)-1, x)

for y in range(0, len(maze2)):
    maze_bfs(y, 0)
    maze_bfs(y, len(maze2[0])-1)


print(dist/2)
print(sum(x.count(".") for x in maze2))

f = open('readme.txt', 'w')
for k in maze2:
    tmp = ""
    for j in k:
        tmp += j
    f.write(tmp + '\n')

f.close()