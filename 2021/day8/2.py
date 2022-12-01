#!/usr/bin/env python3
f = [x.strip().split("|") for x in open("8.txt").readlines()]
n = 0
for _ in f:
    letters = _[0].replace(" ","")
    _[0] = [s for s in _[0].strip().split()]
    _[1] = [s for s in _[1].strip().split()]
    
    numbers = 10*[{}]
    seven_segment = 7*[""]
    
    for number in _[0]:
        if(len(number) == 2):
            numbers[1] = set(number)
        elif(len(number) == 3):
            numbers[7] = set(number)
        elif(len(number) == 4):
            numbers[4] = set(number)
        elif(len(number) == 7):
            numbers[8] = set(number)
            
    seven_segment[0] = set(numbers[7] - numbers[1]).pop()

    for l in ["a","b","c","d","e","f","g"]:
        if(letters.count(l) == 6):
            seven_segment[1] = l
        elif(letters.count(l) == 4):
            seven_segment[4] = l    
        elif(letters.count(l) == 9):
            seven_segment[5] = l
        elif(letters.count(l) == 8 and l != seven_segment[0]):
            seven_segment[2] = l
            
    seven_segment[3] = set(numbers[4] - set([seven_segment[1],seven_segment[2],seven_segment[5]])).pop()
    seven_segment[6] = set(numbers[8]- set(seven_segment[:6])).pop()
    
    numbers[0] = set(seven_segment) - set(seven_segment[3])
    numbers[2] = set(seven_segment) - set([seven_segment[1],seven_segment[5]])
    numbers[3] = set(seven_segment) - set([seven_segment[1],seven_segment[4]]) 
    numbers[5] = set(seven_segment) - set([seven_segment[2],seven_segment[4]]) 
    numbers[6] = set(seven_segment) - set(seven_segment[2]) 
    numbers[9] = set(seven_segment) - set(seven_segment[4])

    n += int("".join([str(numbers.index(set(number))) for number in _[1]]))

print(n)