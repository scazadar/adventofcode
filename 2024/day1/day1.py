#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
l,r = zip(*[[int(x) for x in s.split()] for s in open("2024/inputs/day1.sample").read().split("\n")])

#Part1
part1 = 0
#Part2
part2 = 0

for x,n in enumerate(sorted(l)):
    part1 += abs(n-sorted(r)[x])
    part2 += n*r.count(n)

print(f"Part: {part1}")
print(f"Part2: {part2}")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s