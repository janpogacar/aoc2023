import re
import numpy as np

def getScore(cards):
    s = set(cards)
    if len(s) == len(cards): 
        return 0 # high card
    if len(s) == len(cards)-1: 
        return 1 # one pair
    if len(s) == len(cards) -2: #two pairs or 3OAK
        for x in cards:
            if len(re.findall(x, cards)) == 3:
                return 3 # 3=AK
        return 2 # two pairs
    if len(s) == len(cards) -3: #full house or 4OAK
        for x in cards:
            if len(re.findall(x, cards)) == 4:
                return 5 # 4=AK
        return 4 #FH
    if len(s) == len(cards) -4: #5OAK
        return 6 #4OAK
    
def getScore2(cards):
    s = set(cards)
    if len(s) == len(cards): 
        if "J" in s:
            return 1 #one pair
        else:
            return 0 # high card
    if len(s) == len(cards)-1: 
        if "J" in s:
            return 3 #3oak
        else:
            return 1 # one pair
    if len(s) == len(cards) -2: #two pairs or 3OAK
        for x in cards:
            if len(re.findall(x, cards)) == 3:
                if "J" in s:
                    return 5 #4oak
                else:
                    return 3 # 3=AK
        if "J" in s:
            if len(re.findall("J", cards)) == 2:
                return 5 #fh
            else: return 4
        else:
            return 2 # two pairs
    if len(s) == len(cards) -3: #full house or 4OAK
        for x in cards:
            if len(re.findall(x, cards)) == 4:
                if "J" in s:
                    return 6 #5oak
                else:
                    return 5 # 4=AK
        if "J" in s:
            return 6 #5oak
        else:
            return 4 #FH
    if len(s) == len(cards) -4: #5OAK
        return 6 #5OAK
    
def checkHighCard(card1, card2):
    card_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    for i in range(len(card1)):
        if card1[i] != card2[i]:
            if card_order.index(card2[i]) > card_order.index(card1[i]):
                return True
            else: 
                return False
    return False

def checkHighCard2(card1, card2):
    card_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    for i in range(len(card1)):
        if card1[i] != card2[i]:
            if card_order.index(card2[i]) > card_order.index(card1[i]):
                return True
            else: 
                return False
    return False


def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if (getScore(arr[j][0]) > getScore(arr[j+1][0])
                or ((getScore(arr[j][0]) == getScore(arr[j+1][0])
                     and checkHighCard(arr[j][0], arr[j+1][0])))):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            return
    
def bubbleSort2(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if (getScore2(arr[j][0]) > getScore2(arr[j+1][0])
                or ((getScore2(arr[j][0]) == getScore2(arr[j+1][0])
                     and checkHighCard2(arr[j][0], arr[j+1][0])))):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            return

with open('input.txt') as f:
    lines = f.readlines()

hands = []
for x in lines:
    hands.append(x.split(" "))

bubbleSort(hands)

score = 0
for i in range(len(hands)):
    score += int(hands[i][1])*(i+1)

print(score)

bubbleSort2(hands)

score = 0
for i in range(len(hands)):
    score += int(hands[i][1])*(i+1)

print(score)