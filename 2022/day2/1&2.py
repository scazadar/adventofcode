#!/usr/bin/env python3
print("Part1: ",sum([["B X", "C Y", "A Z", "A X", "B Y", "C Z", "C X", "A Y", "B Z"].index(_.strip())+1 for _ in open("input.txt").readlines()]))
print("Part2: ",sum([["B X", "C X", "A X", "A Y", "B Y", "C Y", "C Z", "A Z", "B Z"].index(_.strip())+1 for _ in open("input.txt").readlines()]))