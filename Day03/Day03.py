with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

result = []
result2 = 0

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        tmp_gears = []
        if (char.isdigit() == False) and (char != "."):
                # find all digits
                # add number to result
                # blank out number with dots
            if lines[y][x-1].isdigit(): #left
                num_end = x
                num_start = lines[y].rfind('.', 0, x-1) +1
                if num_start == -1:
                    num_start = 0
                if num_end == -1:
                    num_end = len(line)
                result.append(int(lines[y][num_start:num_end]))
                tmp_gears.append(int(lines[y][num_start:num_end]))
                tmp_list = list(lines[y])
                for i in range(num_start, num_end):
                    tmp_list[i] = "."
                lines[y] = "".join(tmp_list)
                
            if lines[y][x+1].isdigit(): #right
                num_end = lines[y].find(".", x+1)
                num_start = x+1
                if num_start == -1:
                    num_start = 0
                if num_end == -1:
                    num_end = len(line)
                result.append(int(lines[y][num_start:num_end]))
                tmp_gears.append(int(lines[y][num_start:num_end]))
                tmp_list = list(lines[y])
                for i in range(num_start, num_end):
                    tmp_list[i] = "."
                lines[y] = "".join(tmp_list)
            if lines[y+1][x].isdigit(): #bottom
                num_end = lines[y+1].find(".", x)
                num_start = lines[y+1].rfind('.', 0, x) +1
                if num_start == -1:
                    num_start = 0
                if num_end == -1:
                    num_end = len(line)
                result.append(int(lines[y+1][num_start:num_end]))
                tmp_gears.append(int(lines[y+1][num_start:num_end]))
                tmp_list = list(lines[y+1])
                for i in range(num_start, num_end):
                        tmp_list[i] = "."
                lines[y+1] = "".join(tmp_list)
            if lines[y-1][x].isdigit(): #top
                num_end = lines[y-1].find(".", x)
                num_start = lines[y-1].rfind('.', 0, x) +1
                if num_start == -1:
                    num_start = 0
                if num_end == -1:
                    num_end = len(line)
                result.append(int(lines[y-1][num_start:num_end]))
                tmp_gears.append(int(lines[y-1][num_start:num_end]))
                tmp_list = list(lines[y-1])
                for i in range(num_start, num_end):
                    tmp_list[i] = "."
                lines[y-1] = "".join(tmp_list)
                
            if lines[y-1][x+1].isdigit(): #top right
                num_end = lines[y-1].find(".", x+1)
                num_start = lines[y-1].rfind('.', 0, x+1) +1
                if num_start == -1:
                    num_start = 0
                if num_end == -1:
                    num_end = len(line)
                result.append(int(lines[y-1][num_start:num_end]))
                tmp_gears.append(int(lines[y-1][num_start:num_end]))
                tmp_list = list(lines[y-1])
                for i in range(num_start, num_end):
                    tmp_list[i] = "."
                lines[y-1] = "".join(tmp_list)
                
            if lines[y-1][x-1].isdigit(): #top left
                num_end = lines[y-1].find(".", x-1)
                num_start = lines[y-1].rfind('.', 0, x-1) +1
                if num_start == -1:
                    num_start = 0
                if num_end == -1:
                    num_end = len(line)
                result.append(int(lines[y-1][num_start:num_end]))
                tmp_gears.append(int(lines[y-1][num_start:num_end]))
                tmp_list = list(lines[y-1])
                for i in range(num_start, num_end):
                    tmp_list[i] = "."
                lines[y-1] = "".join(tmp_list)
                
            if lines[y+1][x+1].isdigit(): #bottom right
                num_end = lines[y+1].find(".", x+1)
                num_start = lines[y+1].rfind('.', 0, x+1) +1
                if num_start == -1:
                    num_start = 0
                if num_end == -1:
                    num_end = len(line)
                result.append(int(lines[y+1][num_start:num_end]))
                tmp_gears.append(int(lines[y+1][num_start:num_end]))
                tmp_list = list(lines[y+1])
                for i in range(num_start, num_end):
                        tmp_list[i] = "."
                lines[y+1] = "".join(tmp_list)
                
            if lines[y+1][x-1].isdigit(): #botom left
                num_end = lines[y+1].find(".", x-1)
                num_start = lines[y+1].rfind('.', 0, x-1) +1
                if num_start == -1:
                    num_start = 0
                if num_end == -1:
                    num_end = len(line)
                result.append(int(lines[y+1][num_start:num_end]))
                tmp_gears.append(int(lines[y+1][num_start:num_end]))
                tmp_list = list(lines[y+1])
                for i in range(num_start, num_end):
                        tmp_list[i] = "."
                lines[y+1] = "".join(tmp_list)
                
            if len(tmp_gears) == 2:
                result2 += tmp_gears[0]*tmp_gears[1]

print(sum(result))
print(result2)
    
            