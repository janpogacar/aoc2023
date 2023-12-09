with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

max_red = 12
max_blue = 14
max_green = 13

result = 0
game_power = 0

for i, line in enumerate(lines):
    a, x = line.split(": ")
    legal = True
    red_min = 0
    green_min = 0
    blue_min = 0
    for y in x.split("; "):
        for z in y.split(", "):
            if z[-3:] == 'red':
                if int(z[0:2]) > max_red:
                    legal = False
                if int(z[0:2]) > red_min:
                    red_min = int(z[0:2])
            elif z[-4:] == 'blue':
                if int(z[0:2]) > max_blue:
                    legal = False
                if int(z[0:2]) > blue_min:
                    blue_min = int(z[0:2])
            elif z[-5:] == 'green':
                if int(z[0:2]) > max_green:
                    legal = False
                if int(z[0:2]) > green_min:
                    green_min = int(z[0:2])
    game_power = game_power + (red_min*green_min*blue_min)
    if legal:
        result = result+i+1

print(f"Puzzle 1 solution: {result}")
print(f"Puzzle 2 solution: {game_power}")
