#!/usr/bin/env python3
#Imports
import time

#Zeit Start
start = time.time()

pointSum:int = 0
winNumberList:list = []

#Main
cards = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']

five = []
four = []
three = []
two = []
one = []
fullhouse = []
twopair = []

def handValue(hand):
    cardAmounts = [0 for x in range(13)]
    for x,c in enumerate(cards):
        cardAmounts[x] = hand.count(c)

    if(5 in cardAmounts[1:] 
        or 4 in cardAmounts[1:] and hand.count('J') == 1
        or 3 in cardAmounts[1:] and hand.count('J') == 2
        or 2 in cardAmounts[1:] and hand.count('J') == 3
        or hand.count('J') >= 4):
        five.append(hand)
        return 7
    elif(4 in cardAmounts[1:] 
         or 3 in cardAmounts[1:] and hand.count('J') == 1
         or 2 in cardAmounts[1:] and hand.count('J') == 2
         or hand.count('J') == 3):
        four.append(hand)
        return 6
    elif(3 in cardAmounts[1:] and 2 in cardAmounts[1:]
         or 3 in cardAmounts[1:] and hand.count('J') >= 1
         or 2 in cardAmounts[1:] and hand.count('J') >= 2
         or cardAmounts[1:].count(2) == 2 and hand.count('J') == 1):
        fullhouse.append(hand)
        return 5
    elif(3 in cardAmounts[1:] 
         or 2 in cardAmounts[1:] and hand.count('J') == 1
         or hand.count('J') == 2):
        three.append(hand)
        return 4
    elif(cardAmounts[1:].count(2) == 2 
         or 2 in cardAmounts[1:] and hand.count('J') == 1):
        twopair.append(hand)
        return 3
    elif(2 in cardAmounts[1:] 
         or hand.count('J') == 1):
        one.append(hand)
        return 2
    else:
        return 1

def compareCards(cards1,cards2):
    if(handValue(cards1) > handValue(cards2)):
        return 0
    elif(handValue(cards1) < handValue(cards2)):
        return 1
    elif(handValue(cards1) == handValue(cards2)):
        for x,c in enumerate(cards1):
            if(cards.index(c) > cards.index(cards2[x])):
                return 0
            elif(cards.index(c) < cards.index(cards2[x])):
                return 1
    
hands = [[f.split(" ")[0],int(f.split(" ")[1])] for f in open("2023/inputs/day7").read().split("\n")]
sortedHands = []
for x,hand in enumerate(hands):
    if(len(sortedHands) == 0):
        sortedHands.append(hand)
    else:
        insertIndex = 0
        for h in sortedHands:
            if(compareCards(h[0],hand[0]) == 1):
                break
            insertIndex += 1
        sortedHands.insert(insertIndex,hand)

sortedHands.reverse()
bids = []

for x,hand in enumerate(sortedHands):
    bids.append(hand[1] * (x + 1))
    
print(f"Part2: {sum(bids)}")

#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))