#!/usr/bin/env python3
#Imports
import time, copy

#Zeit Start
start = time.time()

#Main
def filter_emtpystring(s):
    return s != " "

f = open("inputs/day5").read().split("\n\n")
crates_1 = [list(filter(filter_emtpystring,[_[c+1] for _ in f[0].split("\n")[:-1]])) for c in range(0,len(f[0].split("\n")[0])+1,4)]
crates_2 = copy.deepcopy(crates_1)
procedure = [[int(_.split()[1]),int(_.split()[3]),int(_.split()[5])] for _ in f[1].split("\n")]

for p in procedure:
    for m in range(p[0]):
        crates_1[p[2]-1] = [crates_1[p[1]-1].pop(0)] + crates_1[p[2]-1]
    crates_2[p[2]-1] = crates_2[p[1]-1][:p[0]] + crates_2[p[2]-1]
    crates_2[p[1]-1] = crates_2[p[1]-1][p[0]:]

print("Part1: " + "".join(_[0] for _ in crates_1))
print("Part2: " + "".join(_[0] for _ in crates_2))

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s
