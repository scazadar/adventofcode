#!/usr/bin/env python3
#Imports
import time, re, sys, copy

#Zeit Start
start = time.time()

#Main
input = open("inputs/day5").read().split("\n\n")
freshranges = set([tuple(int(_) for _ in range.split("-")) for range in input[0].split("\n")])
ingredient = set([int(i) for i in input[1].split("\n")])

while True:
    validRanges = set()
    for x,r in enumerate(freshranges):
        for _ in freshranges:
            ns = 0
            ne = 0
            
            if(_[0] <= r[0] <= _[1]):
                ns = _[0]
            else:
                ns = r[0]
            if(_[0] <= r[1] <= _[1]):
                ne = _[1]
            else:
                ne = r[1]
            
            if((ns,ne) != r):
                validRanges.add((ns,ne))
                break
        else:
            validRanges.add(r)
            
    if(freshranges == validRanges):
        break       
    freshranges = validRanges
    
freshlistCount = 0
for i in ingredient:
    for r in freshranges:
        if(r[0] <= i <= r[1]):
            freshlistCount += 1
            break

print(f"Part 1: {freshlistCount}")

freshIRangesCount = 0
for r in freshranges:
    freshIRangesCount += r[1]-r[0]+1 
print(f"Part 2: {freshIRangesCount}")
    

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))