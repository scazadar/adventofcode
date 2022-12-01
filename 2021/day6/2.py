#!/usr/bin/env python3
start_fishs = [int(_) for _ in [x.strip() for x in open("6.txt").readlines()][0].split(",")]
pregnancy = 9*[0]
DAYS = 256

for _ in start_fishs:
    pregnancy[_] += 1

for day in range(DAYS):
    pregnancy[7] += pregnancy[0]
    pregnancy = pregnancy[1:] + [pregnancy[0]]
print(sum(pregnancy))