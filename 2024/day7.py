#!/usr/bin/env python3
# Imports
import time
from itertools import product

# Zeit Start
start = time.time()

# Main
cal = [(int(_.strip().split(":")[0]),[int(_) for _ in _.strip().split(":")[1].split()]) for _ in open("2024/inputs/day7.sample").readlines()]


#Part1
valid = []
operator = ["+","*"]
for c in cal:
    oc = product(operator, repeat=len(c[1]) - 1)
    for o in oc:
        summe = c[1][0]
        for num, op in zip(c[1][1:], o):
            summe = eval(f"{summe}{op}{num}")
        if(summe == c[0]):
            valid.append(c[0])
            break
     
print(f"Part1: {sum(valid)}")

#Part2
valid = []
operator = ["+","*","||"]
for c in cal:
    oc = product(operator, repeat=len(c[1]) - 1)
    for o in oc:
        summe = c[1][0]
        for num, op in zip(c[1][1:], o):
            if(op == "||"):
                summe = int(f"{summe}{num}")
            else:
                summe = eval(f"{summe}{op}{num}")
        if(summe == c[0]):
            valid.append(c[0])
            break
        
print(f"Part2: {sum(valid)}")
        
# Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))