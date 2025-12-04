"""
Day 3: Lobby
Link to Problems: https://adventofcode.com/2025/day/3
"""
with open("real_03.txt") as f:
    banks = f.read().splitlines()
######################################### PART ONE #########################################

def find_combo (bank): #find largest joltage
    highest = 0
    for pos, a in enumerate(bank):
        for b in bank[pos + 1:]:
            highest = max(highest,int(f"{a}{b}"))
    return highest

total = sum(find_combo(i) for i in banks)
print(total)
######################################### PART TWO #########################################
#first approach was way too comlicated, see bellow

def find_highest(bank, k):
    result = []
    n = len(bank)
    for i, d in enumerate(bank):
        # remove smaller digits if possible
        while result and result[-1] < d and len(result) + (n - i) > k:
            result.pop()
        if len(result) < k:
            result.append(d)
    return int("".join(result))

total = 0
for bank in banks:
    highest = find_highest(bank, 12)
    total += highest

print(total)

"""
This was my first approach, it works for the sample size, but it simply takes too long
def find_combo_2 (bank,length,previous = None):
    if previous is None:
        previous = []
    if length == len(previous):
        return [int("".join(str(b) for b in previous))]
    if len(bank) < length - len(previous):
        return []
    combs=[]
    for pos, a in enumerate(bank):
        extended = previous + [a]
        combs += find_combo_2(bank[pos +1:],length,extended)
    return combs

total_2 = 0
for bank in banks:
    print(bank)
    combs = find_combo_2(bank,12)
    highest = max(combs)
    print(highest)
    total_2 +=highest

print(total_2)
"""