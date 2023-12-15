#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()
#Main
presents = [[int(_) for _ in _.split("x")] for _ in open("2015/inputs/day2").read().split("\n")]

paper = 0
ribbon = 0
for _ in presents:
    sides = [(2*_[0]*_[1]),(2*_[1]*_[2]),(2*_[0]*_[2])]
    paper += sum(sides) + int(min(sides)/2)
    _ = sorted(_)
    ribbon += 2*_[0] + 2*_[1] + _[0]*_[1]*_[2]

print(f"Part1: {paper}") 
print(f"Part2: {ribbon}") 

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s