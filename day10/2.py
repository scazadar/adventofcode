#!/usr/bin/env python3
f = [_ for _ in [x.strip() for x in open("10.txt").readlines()]]

OPENINGCHARS = "([{<"
CLOSINGCHARS = ")]}>"
ERROR_SCORES = {")":1,"]":2,"}":3,">":4}

scores = []
for line in f:
    score = 0
    next_closing_chars = []
    for _ in range(len(line)):
        if(line[_] in OPENINGCHARS):
            next_closing_chars.append(CLOSINGCHARS[OPENINGCHARS.index(line[_])])
        elif(next_closing_chars[-1] != line[_]):
            score += ERROR_SCORES.get(line[_])
            break
        else:
            next_closing_chars = next_closing_chars[:-1]
    else: 
        for _ in reversed(next_closing_chars):
            score = score * 5 + ERROR_SCORES.get(_)
        scores.append(score)

scores.sort()
print(scores[int(len(scores)/2)])