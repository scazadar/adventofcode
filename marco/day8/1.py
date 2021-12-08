#!/usr/bin/env python3
U_NUMBERS_COUNT = [2,3,4,7]
f = [x.strip().split("|") for x in open("8.txt").readlines()]
s = 0
for _ in f:
    s += len([s for s in _[1].strip().split() if len(s) in U_NUMBERS_COUNT])
print(s)