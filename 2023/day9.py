#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
zahlenfolgen = [[int(_) for _ in _.split(" ")] for _ in open("2023/inputs/day9").read().split("\n")]

nextNumbers = []
previousNumbers = []

for zahlenfolge in zahlenfolgen:
    tempNumbers = [zahlenfolge]
    while(set(tempNumbers[-1]) != {0}):
        tempNumbers.append([tempNumbers[-1][_+1]-tempNumbers[-1][_] for _ in range(len(tempNumbers[-1]) - 1)])

    for x in reversed(range(1,len(tempNumbers))):
        tempNumbers[x-1].append(tempNumbers[x][-1] + tempNumbers[x-1][-1])
        tempNumbers[x-1].insert(0,tempNumbers[x-1][0] - tempNumbers[x][0])
    nextNumbers.append(tempNumbers[0][-1])
    previousNumbers.append(tempNumbers[0][0])
    
print(f"Part1: {sum(nextNumbers)}")
print(f"Part2: {sum(previousNumbers)}")
    

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))