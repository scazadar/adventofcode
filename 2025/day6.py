#!/usr/bin/env python3
#Imports
import time, math

#Zeit Start
start = time.time()

#Main
input = open("inputs/day6").readlines()
numbers = tuple(zip(*[tuple(map(int,n.strip().split())) for n in input[:-1]]))
ops = [op for op in input[-1].strip().split()]

def getTotal(ops,numbers):
    total = 0
    for n,op in enumerate(ops):
        total += sum(numbers[n]) if op == '+' else math.prod(numbers[n])
    return total
    
print(f"Part 1: {getTotal(ops,numbers)}")
    
nInput = tuple("".join(_).strip() for _ in (zip(*((n.replace("\n","")) for n in input[:-1]))))
numbers = []
tempL = []
for nI in nInput:
    if(nI == ''):
        numbers.append(tempL)
        tempL = []
    else:
        tempL.append(int(nI))
else:
    numbers.append(tempL)

print(f"Part 2: {getTotal(ops,numbers)}")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))