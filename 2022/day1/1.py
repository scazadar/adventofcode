#!/usr/bin/env python3
f = open("input.txt").readlines()
cals = []
elves = []
for line in f:
    if(line != "\n"):
        cals.append(int(line))
    else:
        elves.append(sum(cals))
        cals = []


print(max(elves))
