#!/usr/bin/env python3
# Imports
import time
import re,sys

# Zeit Start
start = time.time()

# Main
input = open("2024/inputs/day3").read()

p1muls = re.findall(r"mul\((\d+),(\d+)\)",input)
p2muls = re.findall(r"(don't\(\)|do\(\))|mul\((\d+),(\d+)\)", input)

filterd_muls = []

dod = True
for cmd,l,r in p2muls:
    if(cmd == "don't()"):
        dod = False
    elif(cmd == "do()"):
        dod = True
    elif(dod):
        filterd_muls.append((l,r))

print(f"Part1: {sum([int(l)*int(r) for l,r in p1muls])}")
print(f"Part2: {sum([int(l)*int(r) for l,r in filterd_muls])}")

# Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s
