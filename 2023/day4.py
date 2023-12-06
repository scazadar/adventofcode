#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

pointSum:int = 0
winNumberList:list = []

#Main
for winningNumbers,haveNumbers in [[[int(x) for x in num.strip().split(" ") if x != ''] for num in line.split(":")[1].split("|")] for line in open("2023/inputs/day4").read().split("\n")]:
    winNumbers = [[winNumber for winNumber in winningNumbers if winNumber in haveNumbers],1]
    winNumberList.append(winNumbers)
    #Part1
    points:int = 0
    for x in range(len(winNumbers[0])):
        if(points == 0):
            points = 1
        else:
            points = points * 2
    pointSum += points
    
#Part2
for x,numbers in enumerate(winNumberList):
    for n in winNumberList[x+1:x+len(numbers[0])+1]:
        n[1] += numbers[1]

cardSum:int = sum([x[1] for x in winNumberList])

print(f"Part1: {pointSum}")
print(f"Part2: {cardSum}")
        
#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s