#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

#Main
print("Part1: ",sum([["B X", "C Y", "A Z", "A X", "B Y", "C Z", "C X", "A Y", "B Z"].index(_.strip())+1 for _ in open("inputs/day2").readlines()]))
print("Part2: ",sum([["B X", "C X", "A X", "A Y", "B Y", "C Y", "C Z", "A Z", "B Z"].index(_.strip())+1 for _ in open("inputs/day2").readlines()]))

#Zeit Ende
ende = time.time()
print('Zeit:   {:5.3f}s'.format(ende-start))