#!/usr/bin/env python3
#Imports
import time
from collections import deque
import copy
#Zeit Start
start = time.time()

#Main
f = [[_ for _ in _] for _ in open("2023/inputs/day21.sample").read().split("\n")]

#Start [x,y]
s = [0,0]

for y,_ in enumerate(f):
    for x,p in enumerate(f[y]):
        if(p == "S"):
            s = [x,y]

q = deque([s])


for x in range(6):
    nextQ = deque([])
    for e in q:
        if(e[0]-1 >= 0 ):
            if(f[e[1]][e[0]-1] != "#" and [e[0]-1,e[1]] not in nextQ):
                nextQ.append([e[0]-1,e[1]])
        if(e[0]+1 < len(f[0])):
            if(f[e[1]][e[0]+1] != "#" and [e[0]+1,e[1]] not in nextQ):
                nextQ.append([e[0]+1,e[1]])
        if(e[1]-1 >= 0 ):
            if(f[e[1]-1][e[0]] != "#" and [e[0],e[1]-1]not in nextQ):
                nextQ.append([e[0],e[1]-1])
        if(e[1]+1 < len(f)):
            if(f[e[1]+1][e[0]] != "#" and [e[0],e[1]+1] not in nextQ):
                nextQ.append([e[0],e[1]+1])
    q = nextQ


print(f'Part1: {len(q)}')


#for _ in q:
#    f[_[1]][_[0]] = "O"

#for _ in f:
#    print("".join(_))


#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))