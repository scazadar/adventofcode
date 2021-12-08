#!/usr/bin/env python3
f = [line.strip().split() for line in  open("2.txt").readlines()]
print(sum([int(x[1]) for x in f if x[0] == "forward"])*(sum([int(y[1]) for y in f if y[0] == "down"])-sum([int(y[1]) for y in f if y[0] == "up"])))