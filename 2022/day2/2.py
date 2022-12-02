#!/usr/bin/env python3
scores = ["B X", "C X", "A X", "A Y", "B Y", "C Y", "C Z", "A Z", "B Z"]
print(sum([scores.index(_.strip())+1 for _ in open("input.txt").readlines()]))


"""
A + X 3
A + Y 4
A + Z 8

B + X 1
B + Y 5
B + Z 9

C + X 2
C + Y 6
C + Z 7
"""