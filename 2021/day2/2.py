#!/usr/bin/env python3
f = [line.strip().split() for line in  open("2.txt").readlines()]
aim, x, y = 0, 0 ,0
for line in f:
    if line[0] == "up":
        aim -= int(line[1])
    if line[0] == "down":
        aim += int(line[1])
    if line[0] == "forward":
        x += int(line[1])
        y += int(line[1]) * aim
print(x*y)