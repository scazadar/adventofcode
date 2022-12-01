#!/usr/bin/env python3
f = [int(_) for _ in [x.strip() for x in open("7.txt").readlines()][0].split(",")]
print(min([sum([((abs(_-x)*(abs(_-x)+1))/2) for _ in f]) for x in range(min(f), max(f))]))