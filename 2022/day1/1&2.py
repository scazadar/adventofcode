#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
print("Teil 1: " ,(max([sum([int(_) for _ in _.split("\n")]) for _ in open("inputs/day1").read().split("\n\n")])))
print("Teil 2: " ,(sum(sorted([sum([int(_) for _ in _.split("\n")]) for _ in open("inputs/day1").read().split("\n\n")])[-3:])))

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))