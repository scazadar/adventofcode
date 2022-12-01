#!/usr/bin/env python3
from collections import Counter
f = [x.strip() for x in open("14.txt").readlines()]

polymer = f[0]
rules = {_.split("->")[0]:_.split("->")[1] for _ in [_.replace(" ","") for _ in f[2:]]}

for x in range(10):
    new_polymer = ""
    for _ in range(len(polymer)-1):
        if(polymer[_:_+2] in rules):
            new_polymer += f"{polymer[_]}{rules[polymer[_:_+2]]}"
    polymer = new_polymer + "" + polymer[-1]

count = Counter(polymer)
print(count[max(count,key=count.get)]-count[min(count,key=count.get)])