"""
Day 2: Gift Shop
Link to Problems:
https://adventofcode.com/2025/day/2
You have to remove and add a bunch of invalid IDs from a database.
"""
from traceback import print_tb

with open("sample_input_02.txt") as f:
    sample_input = f.read().split(",")

p1_sample_solution = 1227775554 # from text

# now get a list with all ids in the ranges
ids = []
for r in sample_input:
    star_n, end_n = map(int,r.split("-"))
    for n in range(star_n,end_n+1):
        ids.append(n)
######################################### PART ONE #########################################

# 1) function to check for repeating pattern
def is_invalid(number):
    s = str(number)  #convert to string
    if len(s) % 2 == 0: #check if repeating subpart fits into the whole
        part = s[:(int(len(s)/2))]
        if part * 2 == s: #repeat part so that it's the same length as the whole
                return True
    return False

# 2) now run through every ID and check if they are invalid
solution = 0

for i in ids:
    if is_invalid(i):
        solution += i
print(solution)

######################################### PART TWO #########################################
p2_sample_solution = 4174379265

# 1) function to check for *any* repeating pattern
def is_invalid_2(number):
    s = str(number)  #convert to string
    l = len(s)  #length of the ID
    for position in range(1, l // 2 +1):
        if l % position == 0: #check if repeating subpart fits into the whole part
            part = s[:position]
            repeat = part * (l // position) #repeat part so that it's the same length as the whole
            if repeat == s:
                return True
    return False

solution_2 = 0
for i in ids:
    if is_invalid_2(i):
        solution_2 += i
print(solution_2)
