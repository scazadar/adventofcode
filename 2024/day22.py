#!/usr/bin/env python3
# Imports
import time
import functools

# Zeit Start
startZeit = time.time()

file = "2024/inputs/day22"

initNumbers = [int(_.strip()) for _ in open(file).readlines()]

@functools.cache
def mix(number,secretnumber):
    return number ^ secretnumber

@functools.cache
def prune(secretnumber):
    return secretnumber % 16777216

@functools.cache
def getSecretNumber(number):
    number = prune(mix(number*64,number))
    number = prune(mix(int(number/32),number))
    number = prune(mix(number * 2048,number))
    return number


secretNumbers = []
allPrices = []
allChanges = []
for number in initNumbers:
    prices = []
    changes = []
    for x in range(2000):
        prices.append(int(str(number)[-1]))
        number = getSecretNumber(number)
        changes.append(int(str(number)[-1])-prices[-1])
    
    secretNumbers.append(number)
    allPrices.append(prices)
    allChanges.append(changes)
    
secretNumbers = tuple(secretNumbers)
allPrices = tuple(allPrices)
allChanges = tuple(allChanges)

print(f"Part1: {sum(secretNumbers)}")


allsequences = set()
allChangesWithSequences = []

for changes in allChanges:
    changesWithSequences = []
    for i in range(len(changes) - 4):
        allsequences.add(tuple(changes[i:i+4]))
        changesWithSequences.append(tuple(changes[i:i+4]))
    allChangesWithSequences.append(tuple(changesWithSequences))

allChangesWithSequences = tuple(allChangesWithSequences)

maxBananas = 0
for sequence in allsequences:
    costs = 0
    for i,changesWithSequence in enumerate(allChangesWithSequences):
        if(sequence in changesWithSequence):
            costs += allPrices[i][changesWithSequence.index(sequence) + 4]     
    if(costs > maxBananas):
        maxBananas = costs
        
print(f"Part2: {maxBananas}")


# Zeit Ende
endeZeit = time.time()
print('Zeit:   {:.3f}s'.format(endeZeit-startZeit))