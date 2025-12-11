#!/usr/bin/env python3
#Imports
import time, re

#Zeit Start
start = time.time()

#Main
input = [r for r in open("inputs/day10.sample").readlines()]

lights = [_.replace('.','0').replace('#','1') for _ in [_.split()[0][1:-1] for _ in input]]
buttons = [[[_ for _ in list(map(int,_.split(',')))] for _ in re.findall(r"\((\d+(?:,\d+)*)\)", _)] for _ in input]
joltages = [list(map(int,re.findall(r"\{(\d+(?:,\d+)*)\}", _)[0].split(","))) for _ in input]

binButtons = []
for i,b in enumerate(buttons):
    buttonRow = []
    for button in b:
        s = "0" * len(lights[i])
        for n in button:
            chars = list(s)
            chars[n] = "1"
            s = "".join(chars)
        buttonRow.append(s)  
    binButtons.append(buttonRow)
    
pressCounts = []
for i,light in enumerate(lights):
    pressCount = 0
    iLight = int(light,2)
    variations = set([int("0" * len(light),2)])
    allOn = False
    
    while not allOn:
        pressCount += 1
        tempVariations = set()
        for v in list(variations):
            for button in binButtons[i]:
                if(v^int(button,2) == iLight):
                    allOn = True
                tempVariations.add(v^int(button,2))              
        variations=tempVariations
    pressCounts.append(pressCount)

print(f"Part 1: {sum(pressCounts)}")

# Geht nur fürs Sample
pressCounts = []
for i,jolt in enumerate(joltages):
    pressCount = 0
    variations = set(([tuple([0]*len(jolt))]))
    allCorrect = False
    
    while not allCorrect:
        pressCount += 1
        tempVariations = set()
        for v in list(variations):
            for button in buttons[i]:
                tV = list(v) 
                notValid = False
                for b in button:
                    if(tV[b] > jolt[b]):
                        notValid = True
                    else:
                        tV[b] += 1
                if(notValid):
                    break
                if(tV == jolt):
                    allCorrect = True
                tempVariations.add(tuple(tV))
        variations = tempVariations
    print(pressCount)
    pressCounts.append(pressCount)  
   
print(f"Part 2: {sum(pressCounts)}")
    

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))