#!/usr/bin/env python3
import numpy as np
input = np.array([int(_[-1]) for _ in [x.strip().split(" ") for x in open("demo.txt").readlines()]])

player1_board = np.array(10*[0])
player2_board = np.array(10*[0])
player1_score = 0
player2_score = 0
dice = [1,2,3]
dice_rolled = 3

player1_board[input[0]-1] = 1
player2_board[input[1]-1] = 1

def dice_roll(dice):
    new_dice = []
    for _ in dice:
        if(_ + 3 > 100):
            new_dice.append(_ + 3 - 100)
        else:
            new_dice.append(_ + 3) 
    
    return new_dice

while(True):
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