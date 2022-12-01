#!/usr/bin/env python3
f = [x.strip() for x in open("3.txt").readlines()]
g = ""
for b in range(12):
    g += "1" if sum([int(line[b]) for line in f if line[b] == "1"]) > len(f)/2 else "0"
print((int(g,2)^4095)*int(g,2))