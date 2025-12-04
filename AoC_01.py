"""
Day 1: Secret Entrance
Link to Problems:
https://adventofcode.com/2025/day/1
"""
from math import floor

with open("sample_input_01.txt") as f:
    sample_input = f.read().splitlines()
sample_solution = 3

######################################### PART ONE #########################################

position = 50 #starting position defined in text
counter = 0
for i in sample_input:
    if i[0] == "L": #check first element for direction
        position = (position - int(i[1:])) % 100 # new position is the modulo of 100 to the left (subtraction) of the starting posiition
    elif i[0] == "R":
        position = (position + int(i[1:])) % 100

    if position == 0: # count  where dial stops on 0
        counter += 1
print (("How many times does the Dial end on zero?"), counter)

######################################### PART TWO #########################################

position = 50
counter = 0
for i in sample_input:
    previous = position # 2) to compare how many rotations took place we need the previous position
    if i[0] == "L":
        position = position - int(i[1:]) # 1) keep the whole numbers to account for all rotations
        if position % 100 == 0: #count when stopping on zero
            counter += 1
        if previous % 100 == 0: #remove overcounting when going from 0 to 99
            counter -= 1
    elif i[0] == "R":
        position = position + int(i[1:])

    # 4) now count how many times the dial passes 0 without stopping using floor or //
    prev_rot = floor(previous/100)
    current_rot = floor(position/100)
    passes = abs(current_rot - prev_rot)
    counter+=passes

print(("How many times did the dial end or pass zero?"), counter)
