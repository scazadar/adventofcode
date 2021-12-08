#!/usr/bin/env python3
f = open("1.txt").readlines()
print(len([x for x in range(len(f)) if f[x] > f[x-1]])+1)