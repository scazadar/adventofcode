#!/usr/bin/env python3
scores = ["B X", "C Y", "A Z", "A X", "B Y", "C Z", "C X", "A Y", "B Z"]
print(sum([scores.index(_.strip())+1 for _ in open("input.txt").readlines()]))


"""
A + X 4
A + Y 8
A + Z 3

B + X 1
B + Y 5
B + Z 9

C + X 7
C + Y 2
C + Z 6
"""