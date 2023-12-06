#!/usr/bin/env python3
#Imports
import time
import math

#Zeit Start
start = time.time()

pointSum:int = 0
winNumberList:list = []

#Main
file = open("2023/inputs/day6").read().split("\n")

#Part1
times:list = [int(t) for t in file[0].split(":")[1].split(" ") if t != '']
distanced:list = [int(t) for t in file[1].split(":")[1].split(" ") if t != '']

waysToWin = []
for i,t in enumerate(times):
    r:list = []
    for ti in range(t+1):
        d = (times[i]-ti)*ti
        if(d > distanced[i]):
            r.append(d)
    waysToWin.append(len(r))      
    
print(f"Part1: {math.prod(waysToWin)}")

#Part2
t:int = int(file[0].split(":")[1].replace(" ",""))
distance:int = int(file[1].split(":")[1].replace(" ",""))

r:list = []
for ti in range(t+1):
    d = (t-ti)*ti
    if(d > distance):
        r.append(d)

print(f"Part2: {len(r)}")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))