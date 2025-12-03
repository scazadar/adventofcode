#!/usr/bin/env python3
#Imports
import time, re

#Zeit Start
start = time.time()

#Main
banks = [[int(x) for x in s.strip()] for s in open("inputs/day3").readlines()]

# Part 1
maxJoltages = []

for bank in banks:
    maxJoltage = 0
    for x in range(len(bank)-1):
        joltage = int(f"{bank[x]}{max(bank[x+1:])}")
        if(joltage > maxJoltage):
            maxJoltage = joltage
    maxJoltages.append(maxJoltage)

print(f"Part 1: {sum(maxJoltages)}")

# Part 2
maxJoltages = 0
for bank in banks:
    maxJoltage = ""
    lastIndex = 0
    
    for x in reversed(range(12)):
        li = len(bank) - x
        hJ = max(bank[lastIndex:li])
        maxJoltage += str(hJ)
        lastIndex = bank.index(hJ,lastIndex) + 1
    maxJoltages += int(maxJoltage)
    
print(f"Part 2: {maxJoltages}")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))