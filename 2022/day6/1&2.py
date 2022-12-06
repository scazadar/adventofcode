#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
def check_one_char(s):
    for c in s:
        if s.count(c) > 1:
            return True
    return False

f = open("inputs/day6").read()

for _ in range(len(f)-4):
    if not check_one_char(f[_:_+4]):
        print("Part1: ",_+4)
        break

for _ in range(len(f)-14):
    if not check_one_char(f[_:_+14]):
        print("Part2: ",_+14)
        break
    
#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s
