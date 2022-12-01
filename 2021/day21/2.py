#!/usr/bin/env python3
import numpy as np
from collections import defaultdict
input = np.array([int(_[-1]) for _ in [x.strip().split(" ") for x in open("demo.txt").readlines()]])

player1_board = np.array(10*["O"])
player2_board = np.array(10*["O"])

player1_board[input[0]-1] = "X"
player2_board[input[1]-1] = "X"


multiverse_count = defaultdict(int)
multiverse_values = defaultdict(int)

init_arr = np.array(["X","O","O","O","O","O","O","O","O","O"])
for x in range(10):
    multiverse_count["".join(init_arr)] = 0
    multiverse_values["".join(init_arr)] = x+1
    init_arr = np.roll(init_arr,1)

#multiverse_count["".join(player1_board)] += 1
multiverse_sums = []
for x in range(50):
    multiverse_sums.append(multiverse_count.copy())

multiverse_sums[0]["".join(player1_board)] += 1 

#print(multiverse_values)
#print([_ for _ in "".join(player1_board)])
#print(multiverse_count[player1_board])

#multiverse[str(player1_board)] += [1,0]
#player2_multiverse[str(player2_board)] += [1,0]
#print(multiverse_sums[0])
def dice_roll(multiverse_sums):
    new_multiverse_sums = []
    #for x in range(50):
    #    new_multiverse_sums.append(multiverse_count.copy())
    for s in range(len(multiverse_sums)):
        for universe in multiverse_sums[s]:

            #universe = multiverse_sums[sum][n]
            value = multiverse_sums[s][universe]
            #print(value)
            u = [_ for _ in universe]
            if(value > 0 and s < 21):
                #new_multiverse_sums[sum][universe] = multiverse_sums[sum][universe] - 1
                #print(sum)
                #print(u)
                #print(multiverse_values["".join(np.roll(np.array(u),1))])
                #print(multiverse_values["".join(np.roll(np.array(u),2))])
                #print(multiverse_values["".join(np.roll(np.array(u),3))])
                
                rolled_1 = "".join(np.roll(np.array(u),1))
                rolled_2 = "".join(np.roll(np.array(u),2))
                rolled_3 = "".join(np.roll(np.array(u),3))
                #print(sum+multiverse_values[rolled_1])
                
                
                new_multiverse_sums[s+multiverse_values[rolled_1]][rolled_1] = multiverse_sums[s+multiverse_values[rolled_1]][rolled_1] + value
                new_multiverse_sums[s+multiverse_values[rolled_2]][rolled_2] = multiverse_sums[s+multiverse_values[rolled_2]][rolled_2] + value
                new_multiverse_sums[s+multiverse_values[rolled_3]][rolled_3] = multiverse_sums[s+multiverse_values[rolled_3]][rolled_3] + value
    return new_multiverse_sums
    
#print(multiverse)
#dice_roll(multiverse_sums)


for x in range(15):
    multiverse_sums = [_.copy() for _ in dice_roll(multiverse_sums)]

x = 0
print(f"{sum([sum(_) for _ in [[_[x] for x in _] for _ in multiverse_sums]])}")

"""
while(True):
    for board in player1_universe:
        pass
    player1_board = np.roll(player1_board,sum(dice))
    player1_score += np.where(player1_board == 1)[0][0]+1

    if(player1_score >= 1000):
        break
    dice_rolled += 3
    dice = dice_roll(dice)
    player2_board = np.roll(player2_board,sum(dice))
    player2_score += np.where(player2_board == 1)[0][0]+1

    if(player2_score >= 1000):
        break

    dice_rolled += 3
    dice = dice_roll(dice)

print(min([player1_score,player2_score]) * dice_rolled)
"""