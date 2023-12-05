import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

win_sum = 0
cards_num = list(np.ones(len(lines), dtype=int))

for card_num, line in enumerate(lines):
    win_nums_list = []
    my_nums_list = []
    a, nums = line.split(": ")
    win_nums, my_nums = nums.split("|")
    for i,x in enumerate (win_nums.split(" ")):
        if x != "":
            win_nums_list.append(int(x))
    for i,x in enumerate (my_nums.split(" ")):
        if x != "":
            my_nums_list.append(int(x))
    
    num_of_wins = len(list(set(win_nums_list)&set(my_nums_list)))
    if num_of_wins != 0:
        win_sum += 2**(num_of_wins-1)
    
    for i in range(card_num+1, card_num+num_of_wins+1):
        cards_num[i] += cards_num[card_num]

print(win_sum)
print(sum(cards_num))