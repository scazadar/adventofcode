#!/usr/bin/env python3
#Imports
import time, re

#Zeit Start
start = time.time()

#Main
ranges = [[tuple([int(r[0]),int(r[1])]) for r in re.findall(r"(\d+)-(\d+)",s)] for s in open("inputs/day2").read().split("\n")][0]

invalidIDsP1 = []
invalidIDsP2 = []
for r in ranges:
    for i in range(r[0],r[1]+1):
        n = str(i)
        if(n[:len(n)//2] == n[len(n)//2:]):
            invalidIDsP1.append(i)
        for _,x in enumerate(range(len(n) // 2)):
            if(n.count(n[:x+1]) * (x + 1)  == len(n)):
                invalidIDsP2.append(i)
                break

print(f"Part 1: {sum(invalidIDsP1)}") 
print(f"Part 2: {sum(invalidIDsP2)}")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))