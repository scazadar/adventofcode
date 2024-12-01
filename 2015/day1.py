#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()
#Main
floor = 0
basement = 0
for x,_ in enumerate(open("2015/inputs/day1").read()):
    if(_ == "("):
        floor += 1
    else:
        floor -= 1
    if(floor == -1 and basement == 0):
        basement = x + 1

print(f"Part1: {floor}")
print(f"Part2: {basement}")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s