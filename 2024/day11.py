#!/usr/bin/env python3
# Imports
import time
from collections import Counter

# Zeit Start
start = time.time()

# Main
stones = [int(_) for _ in open("2024/inputs/day11").read().split()]
stonesCounter = Counter(stones)

#Part1
def blink(stones):
    newStones = []

    for stone in stones:
        if(stone == 0):
            newStones.append(1)
        elif(len(str(stone)) % 2 == 0):
            newStones.append(int(str(stone)[:len(str(stone)) // 2]))
            newStones.append(int(str(stone)[len(str(stone)) // 2:]))
        else:
            newStones.append(2024 * stone)

    return newStones

for i in range(25):
    stones = blink(stones)

print(f"Part1: {len(stones)}")


#Part2
def blink2(stones):
    newStones = Counter()
    for stone in stones.keys():
        if(stone == 0):
            newStones[1] += stones[0]
        elif(len(str(stone)) % 2 == 0):
            newStones[int(str(stone)[:len(str(stone)) // 2])] += stones[stone]
            newStones[int(str(stone)[len(str(stone)) // 2:])] += stones[stone]
        else:
            newStones[2024 * stone] += stones[stone]
    return newStones

for i in range(75):
    stonesCounter = blink2(stonesCounter)

print(f"Part2: {sum([stonesCounter[_] for _ in stonesCounter])}")


# Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))