#!/usr/bin/env python3
#Imports
import time, re

#Zeit Start
start = time.time()

#Main
banks = [[int(x) for x in s.strip()] for s in open("inputs/day3").readlines()]

maxJoltagesP1 = 0
maxJoltagesP2 = 0

for bank in banks:
    maxJoltage = ""   
    lastIndex = 0
    for x in reversed(range(2)):
        li = len(bank) - x
        hJ = max(bank[lastIndex:li])
        maxJoltage += str(hJ)
        lastIndex = bank.index(hJ,lastIndex) + 1   
    maxJoltagesP1 += int(maxJoltage)

    maxJoltage = "" 
    lastIndex = 0
    for x in reversed(range(12)):
        li = len(bank) - x
        hJ = max(bank[lastIndex:li])
        maxJoltage += str(hJ)
        lastIndex = bank.index(hJ,lastIndex) + 1
    maxJoltagesP2 += int(maxJoltage)
    
print(f"Part 1: {maxJoltagesP1}")
print(f"Part 2: {maxJoltagesP2}")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))