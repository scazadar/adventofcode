#!/usr/bin/env python3
# Imports
import time

# Zeit Start
start = time.time()

# Main
reports = [[int(x) for x in s.split()]
           for s in open("2024/inputs/day2").read().split("\n")]

def compareLevels(report,x,ic):
    if(ic > 0):
        return  report[x] < report[x+1] - 3 or report[x] >= report[x+1] #or (sr[x] != list(reversed(report))[x] and sr[x] != report[x])
    else:
        return report[x] > report[x+1] + 3 or report[x] <= report[x+1] #or (sr[x] != list(reversed(report))[x] and sr[x] != report[x])

safeCount = 0        
safeCount2 = 0
for report in reports:
    safe = False
    
    ic = 1 if report[0] < report [1] else -1
    for x in range(len(report) - 1):
        if(compareLevels(report,x,ic)):
            break
    else:
        safe = True

    safeCount += 1 if safe else 0
        
    if(not safe):
        for x in range(len(report)):
            creport = report.copy()
            del creport[x]
            ic = 1 if creport[0] < creport [1] else -1
            for x in range(len(creport) - 1):
                if(compareLevels(creport,x,ic)):
                    break
            else:
                safe = True
                         
    safeCount2 += 1 if safe else 0
            
print(f"Part1: {safeCount}")
print(f"Part2: {safeCount2}")




# Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s
