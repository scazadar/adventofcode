#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
dial = 50
rotations = [int(s[1:]) * -1 if s[0] == 'L' else int(s[1:]) for s in open("inputs/day1").read().split("\n")]

countP1 = 0
countP2 = 0
for r in rotations:     
    dial = dial % 100 
    # Part 1
    if((dial + r) % 100 == 0):
        countP1 += 1
    
    # Part 2
    for _ in range(abs(r)):
        dial = (dial + (1 if r > 0 else -1)) % 100
        if dial == 0:
            countP2 += 1
    
print(f"Part 1: {countP1}")
print(f"Part 2: {countP2}")


#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))