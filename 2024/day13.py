#!/usr/bin/env python3
# Imports
import time
import re

# Zeit Start
start = time.time()

file = "2024/inputs/day13"

machines = [[tuple(int(_) for _ in re.findall(r"Button A: X\+(\d+), Y\+(\d+)", _.split("\n")[0])[0]), 
             tuple(int(_) for _ in re.findall(r"Button B: X\+(\d+), Y\+(\d+)", _.split("\n")[1])[0]), 
             tuple(int(_) for _ in re.findall(r"Prize: X\=(\d+), Y\=(\d+)", _.split("\n")[2])[0])]
            for _ in open(file).read().split("\n\n")]

def calcCosts(machines):
    costs = []
    for machine in machines:
        aCount = 0
        bCount = 0

        while True:
            aCount += 1
            x = (machine[2][0] - (aCount * machine[0][0])) / machine[1][0]
            y = (machine[2][1] - (aCount * machine[0][1])) / machine[1][1]
            if(x == y):
                bCount = x
                costs.append(aCount * 3 + bCount)
                break
            elif((machine[2][0] - (aCount * machine[0][0])) < 0):
                break
    return costs           

print(f"Part1: {int(sum(calcCosts(machines)))}")

#Part2 
machines = [[tuple(int(_) for _ in re.findall(r"Button A: X\+(\d+), Y\+(\d+)", _.split("\n")[0])[0]), 
             tuple(int(_) for _ in re.findall(r"Button B: X\+(\d+), Y\+(\d+)", _.split("\n")[1])[0]), 
             tuple(10000000000000 + int(_) for _ in re.findall(r"Prize: X\=(\d+), Y\=(\d+)", _.split("\n")[2])[0])]
            for _ in open(file).read().split("\n\n")]

def calcCosts2(machines):
    costs = []

    for machine in machines:
        aCount = (machine[1][1] * machine[2][0] - machine[1][0] * machine[2][1]) / (machine[1][1] * machine[0][0] - machine[1][0] * machine[0][1])
        bCount = (machine[2][0] - machine[0][0] * aCount) / machine[1][0]

        if(aCount % 1 == 0 and bCount % 1 == 0):
            costs.append(aCount * 3 + bCount)   
    return costs

print(f"Part2: {int(sum(calcCosts2(machines)))}")

# Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
