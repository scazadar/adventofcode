#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
f = [_.strip() for _ in open("inputs/day3").readlines()]
print("Part1: ", sum([_-96 if _ > 96 else _-38 for _ in [ord(list(set(list(_)[:int(len(_)/2)]).intersection(set(list(_)[int(len(_)/2):])))[0]) for _ in f]]))
print("Part2: ", sum([_-96 if _ > 96 else _-38 for _ in [ord(list([set(_) for _ in f][_].intersection([set(_) for _ in f][_+1]).intersection([set(_) for _ in f][_+2]))[0]) for _ in range(0,len(f),3)]]))

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))