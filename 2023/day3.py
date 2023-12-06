#!/usr/bin/env python3
#Imports
import time
import string
import math

#Zeit Start
start = time.time()

#Main
partsum:int = 0
parts:list = []
lines:list = open('2023/inputs/day3').read().split('\n')
sz:str = string.punctuation.replace('.','')

gears:dict = {}

for lineNumber,line in enumerate(lines):
    isNumber:bool = False
    
    isPart:bool = False
    isGear:bool = False
    currentNumber:str = ''
    currentGearPosition:str = ''
    
    for i,c in enumerate(lines[lineNumber]):
        if(c.isdigit()):
            for x in range(-1,2):
                lineToCheck = lineNumber + x
                if(lineToCheck >= 0 and lineToCheck < len(lines)):
                    if(i-1 >= 0):
                        if(lines[lineToCheck][i-1] in sz):
                            isPart = True
                        if(lines[lineToCheck][i-1] == '*'):
                            isGear = True
                            currentGearPosition = f'{lineToCheck},{i-1}'
                    if(i+1 < len(lines[lineToCheck])):
                        if(lines[lineToCheck][i+1] in sz):
                            isPart = True
                        if(lines[lineToCheck][i+1] == '*'):
                            isGear = True
                            currentGearPosition = f'{lineToCheck},{i+1}'
                    if(lines[lineToCheck][i] in sz):
                        isPart = True
                    if(lines[lineToCheck][i] == '*'):
                        isGear = True
                        currentGearPosition = f'{lineToCheck},{i}'
            currentNumber += c
        elif(currentNumber != ''):
            if(isPart):
                parts.append(int(currentNumber))
            if(isGear):
                if(currentGearPosition in gears):
                    gears.get(currentGearPosition).append(int(currentNumber))
                else:
                    gears.setdefault(currentGearPosition,[int(currentNumber)])
            currentNumber = ''
            isPart = False
            isGear = False
            
    #Zeilenende
    if(currentNumber != '' and isPart):
        parts.append(int(currentNumber))
    if(currentNumber != '' and isGear):
        if(currentGearPosition in gears):
            gears.get(currentGearPosition).append(int(currentNumber))
        else:
            gears.setdefault(currentGearPosition,[int(currentNumber)])
            
part2sum:int = 0
for gear in gears:
    if(len(gears.get(gear)) == 2):
        part2sum += math.prod(gears.get(gear))         
            
print(f'Part1: {sum(parts)}')
print(f'Part2: {part2sum}')
    
     
#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s