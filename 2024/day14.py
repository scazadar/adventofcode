#!/usr/bin/env python3
# Imports
import time
import re
import math

# Zeit Start
start = time.time()

file = "2024/inputs/day14"

robots = [[tuple(int(_) for _ in _.split(",")) for _ in re.findall(
    r'[-\d]+,[-\d]+', _)] for _ in open(file).readlines()]


wide = 101
tall = 103
s = 100


def calcPositions(robots,wide,tall,s):
    newPositions = []
    for robot in robots:
        x = (robot[0][0] + (robot[1][0] * s)) % wide
        y = (robot[0][1] + (robot[1][1] * s)) % tall
        newPositions.append((x, y))
    return newPositions

quadrants = [0, 0, 0, 0]
for x, y in calcPositions(robots,wide,tall,s):
    if (y < tall//2 and x < wide//2):
        quadrants[0] += 1
    elif (y < tall//2 and x > wide//2):
        quadrants[1] += 1
    elif (y > tall//2 and x < wide//2):
        quadrants[2] += 1
    elif (y > tall//2 and x > wide//2):
        quadrants[3] += 1


print(f"Part1 : {math.prod(quadrants)}")

#Part2
#wide = 11
#tall = 7
s = 0
matched = 0

with open("2024/outputs/day14.txt", "w") as file:
    while s < 10000:
        #Nur um die 100MB :D
        m = [[" " for _ in range(wide)] for _ in range(tall)]
        for x,y in calcPositions(robots,wide,tall,s):
            m[y][x] = '#'

        file.write("==========================================\n")
        file.write(str(s) +"\n")
        for _ in m:
            file.write("".join(_)+"\n")
        file.write("==========================================\n")
            
        s += 1
        
    

# Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
