#!/usr/bin/env python3
from collections import Counter
import numpy as np
f = [x.strip() for x in open("14.txt").readlines()]

polymer = np.array([f"{f[0][_]}{f[0][_+1]}" for _ in range(len(f[0])-1)])
rules = {_.split("->")[0]:[f'{_.split("->")[0][0]}{_.split("->")[1]}',f'{_.split("->")[1]}{_.split("->")[0][1]}'] for _ in [_.replace(" ","") for _ in f[2:]]}

polymer_counts = {rule:0 for rule in rules}
for p in polymer:
    polymer_counts[p] += 1

for x in range(40):
    old_polymer_counts = polymer_counts.copy()
    for count in old_polymer_counts:
        
        if(old_polymer_counts[count] > 0):
            old_count = old_polymer_counts[count]
            polymer_counts[rules[count][0]] += old_count
            polymer_counts[rules[count][1]] += old_count
            polymer_counts[count] -= old_count
    
count_d = {}
for _ in polymer_counts:
    if(_[0] in count_d):
        count_d[_[0]] += polymer_counts[_]
    else:
        count_d.setdefault(_[0],polymer_counts[_])
        

count_d[f[0][0]] += 1
count_d[f[0][-1]] += 1
count = Counter(count_d)
print(count[max(count,key=count.get)]-count[min(count,key=count.get)])