#!/usr/bin/env python3
f = open("1.txt").readlines()
cals = []
elves = []
for line in f:
    if(line != "\n"):
        cals.append(int(line))
    else:
        elves.append(sum(cals))
        cals = []

top3 = 0
for x in range(3):
    top3 += elves.pop(elves.index(max(elves)))
print(top3)
