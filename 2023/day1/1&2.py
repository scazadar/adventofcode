#!/usr/bin/env python3
#Imports
import time, string

#Zeit Start
start = time.time()

stringToNumber = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}

#Main
print(sum([int("".join([s.translate({ord(i): None for i in string.ascii_letters})[0],s.translate({ord(i): None for i in string.ascii_letters})[-1]])) for s in open("2023/inputs/day1").read().split("\n")]))

summe = 0
for s in open("2023/inputs/day1").read().split("\n"):
    partnumber = ''
    for i in range(len(s)):
        if(s[i].isdigit()):
            partnumber += s[i]
        else:
            for sn,number in stringToNumber.items():
                if s[i:].startswith(sn):
                    partnumber += str(number)
    summe += int("".join([partnumber[0],partnumber[-1]])) 
print(summe)


#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s