import re
import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

nums = []
for x in lines:
    nums.append(list(map(int, x.split(" "))))

next_values = []

result = 0
result2 = 0
for j, num in enumerate(nums):
    num_stack = []
    tmp_num = list(np.diff(num))
    num_stack.append(tmp_num)
    while(all(v == 0 for v in tmp_num) is False):
        tmp_num = list(np.diff(tmp_num)) 
        num_stack.append(tmp_num)

    for i in range(len(num_stack)-1, 0, -1):
        num_stack[i-1].append(num_stack[i-1][-1]+num_stack[i][-1])
        num_stack[i-1].insert(0, num_stack[i-1][0]-num_stack[i][0])


    result = result + num[-1] + num_stack[0][-1]
    result2 = result2 + (num[0] - num_stack[0][0])




print(result)
print(result2)
