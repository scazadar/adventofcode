#!/usr/bin/env python3
f = [int(x.strip()) for x in open("1.txt").readlines()]
print(len([x for x in range(1,len(f)-3) if sum(f[x:x+3]) > sum(f[x-1:x+2])])+1)