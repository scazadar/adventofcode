#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
steps = open("2023/inputs/day15").read().split(",")

def getHash(step):
    value = 0
    for _ in step:
        value += ord(_)
        value = (value*17) % 256
    return value


hash = []
for step in steps:
    hash.append(getHash(step))

print(f"Part1: {sum(hash)}")

#Part2
boxes = [[] for _ in range(256)]

for step in steps:
    s = []
    if("=" in step):
        s = step.split("=")
        for x,_ in enumerate(boxes[getHash(s[0])]):
            if(s[0] == _.split("=")[0]):
                boxes[getHash(s[0])][x] = step
                break
        else:
            boxes[getHash(s[0])].append(step)
    elif("-" in step):
        s = step.split("-")
        for x,_ in enumerate(boxes[getHash(s[0])]):
            if(s[0] == _.split("=")[0]):
                boxes[getHash(s[0])].remove(_)
                break
     
sum = 0
for i,box in enumerate(boxes):
    for x,slot in enumerate(box):
        sum += (i+1) * (x+1) * int(slot.split("=")[1])
 
print(f"Part2: {sum}")
 

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))