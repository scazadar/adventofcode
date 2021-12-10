#!/usr/bin/env python3
f = [_ for _ in [x.strip() for x in open("10.txt").readlines()]]

OPENINGCHARS = "([{<"
CLOSINGCHARS = ")]}>"
ERROR_SCORES = {")":3,"]":57,"}":1197,">":25137}
score = 0

for line in f:
    next_closing_chars = []
    for _ in range(len(line)):
        if(line[_] in OPENINGCHARS):
            next_closing_chars.append(CLOSINGCHARS[OPENINGCHARS.index(line[_])])
        elif(next_closing_chars[-1] != line[_]):
            score += ERROR_SCORES.get(line[_])
            break
        else:
            next_closing_chars = next_closing_chars[:-1]
print(score)