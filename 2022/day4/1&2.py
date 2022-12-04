#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
f = [[set(range(int(_.split("-")[0]),int(_.split("-")[1])+1)) for _ in _.strip().split(",")] for _ in open("inputs/day4").readlines()]
print("Part1: ", sum([1 if _[0]<=_[1] or _[1]<=_[0] else 0 for _ in f]))
print("Part2: ", sum([1 if len(_[0]&_[1]) > 0 else 0 for _ in f]))

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.008s
