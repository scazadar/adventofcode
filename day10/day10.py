#!/usr/bin/env python3
f = [_ for _ in [x.strip() for x in open("10.txt").readlines()]]

OPENINGCHARS = "([{<"
CLOSINGCHARS = ")]}>"
ERROR_SCORES_1 = {")":3,"]":57,"}":1197,">":25137}
ERROR_SCORES_2 = {")":1,"]":2,"}":3,">":4}
scores = []
score_1 = 0

for line in f:
    score_2 = 0
    next_closing_chars = []
    for _ in range(len(line)):
        if(line[_] in OPENINGCHARS):
            next_closing_chars.append(CLOSINGCHARS[OPENINGCHARS.index(line[_])])
        elif(next_closing_chars[-1] != line[_]):
            score_1 += ERROR_SCORES_1.get(line[_])
            break
        else:
            next_closing_chars = next_closing_chars[:-1]
    else: 
        for _ in reversed(next_closing_chars):
            score_2 = score_2 * 5 + ERROR_SCORES_2.get(_)
        scores.append(score_2)

scores.sort()
print(f"Part1: {score_1}")
print(f"Part2: {scores[int(len(scores)/2)]}")