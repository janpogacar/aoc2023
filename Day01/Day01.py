with open('input_01.txt') as f:
    lines = f.readlines()

num_list = []
num_list_p2 = []
valid_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
valid_digits_rev = ['eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']

# Puzzle 1
for x in lines:
    # find first number
    for y in x:
        if y.isdigit():
            d1 = int(y)
            break

    # Reverse puzzle 1, repeat the process
    for y in x[::-1]:
        if y.isdigit():
            d2 = int(y)
            break

    num_list.append(10*d1+d2)

print(f"Puzzle 1 solution: {sum(num_list)}")

# Puzzle 2
for x in lines:
    # find first number
    solution = False
    for i,y in enumerate(x):
        if solution:
            break
        if y.isdigit():
            d1 = int(y)
            break
        for z in valid_digits:
            if x[i:].startswith(z):
                d1 = valid_digits.index(z) + 1
                solution = True
                break
        


    # Reverse, repeat the process
    solution = False
    for i,y in enumerate(x[::-1]):
        if solution:
            break
        if y.isdigit():
            d2 = int(y)
            break
        for z in valid_digits_rev:
            if x[::-1][i:].startswith(z):
                d2 = valid_digits_rev.index(z) + 1
                solution = True
                break       

    num_list_p2.append(10*d1+d2)
print(f"Puzzle 2 solution: {sum(num_list_p2)}")