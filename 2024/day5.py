#!/usr/bin/env python3
# Imports
import time, copy

# Zeit Start
start = time.time()

# Main
_ = [_.strip() for _ in open("2024/inputs/day5").readlines()]
rules = [[int(_) for _ in _.split("|")] for _ in _[:_.index("")]]
pages = [[int(_) for _ in _.split(",")] for _ in _[_.index("")+1:]]

pagesToPrint = pages.copy()
pagesNotToPrint = []

for rule in rules:
    for page in pages:
        if(set(rule).issubset(set(page)) and page.index(rule[0]) > page.index(rule[1]) and page in pagesToPrint):
            pagesNotToPrint.append(pagesToPrint.pop(pagesToPrint.index(page)))
            

print(f"Part1: {sum([_[int(len(_)/2)] for _ in pagesToPrint])}")

orderedPagesNotToPrint = []
for page in [_.copy() for _ in pagesNotToPrint]:
    page_old = []
    while page_old != page:
        page_old = page.copy()
        for rule in rules:
            if(set(rule).issubset(set(page))):
                if(page.index(rule[0]) > page.index(rule[1])):
                    i = page.pop(page.index(rule[0]))
                    page.insert(page.index(rule[1]),i)
        
    orderedPagesNotToPrint.append(page)

print(f"Part2: {sum([_[int(len(_)/2)] for _ in orderedPagesNotToPrint])}")
# Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))

# 0.003s
