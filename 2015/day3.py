#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()
#Main
directions = open("2015/inputs/day3").read()

x=0
y=0
x2 = 0
y2 = 0
houses = []

for _,d in enumerate(directions):
    if(d == ">"):
        if(_%2 == 1):
            x +=1
        else:
            x2 += 1
    elif(d == "<"):
        if(_%2 == 1):
            x -= 1
        else:
            x2 -= 1
    elif(d == "^"):
        if(_%2 == 1):
            y -= 1
        else:
            y2 -= 1
    elif(d == "v"):
        if(_%2 == 1):
            y += 1
        else:
            y2 += 1

    if([x,y] not in houses):
        houses.append([x,y])
    if([x2,y2] not in houses):
        houses.append([x2,y2])

print(f"Part2: {len(houses)}")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s