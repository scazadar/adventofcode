#!/usr/bin/env python3
# Imports
import time
import re

# Zeit Start
start = time.time()

# Main
input = open("2024/inputs/day3").read()

p1muls = re.findall(r"mul\(\d+,\d+\)",input)
p2muls = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input)

filterd_muls = []

dod = True
for m in p2muls:
    if(m == "don't()"):
        dod = False
    elif(m == "do()"):
        dod = True
    elif(dod):
        filterd_muls.append(m)

def mul(x,y):
    return x*y

print(f"Part1: {sum([eval(m) for m in p1muls])}")
print(f"Part2: {sum([eval(m) for m in filterd_muls])}")


# Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s
