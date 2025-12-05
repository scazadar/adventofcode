#!/usr/bin/env python3
# Imports
import time
import functools
import re

# Zeit Start
startZeit = time.time()

file = "2024/inputs/day21.sample"

cmds = [[_ for _ in _.strip()] for _ in open(file).readlines()]

numericKeypad = (('7', '8', '9'), ('4', '5', '6'),
                 ('1', '2', '3'), ('.', '0', 'A'))
#directionalKeypad = (('.', (-1, 0), 'A'), ((0, -1), (1, 0), (0, 1)))
directionalKeypad = (('.', "^", 'A'), ("<", "v", ">"))

directions = {(-1,0):"^",(1,0):"v",(0,-1):"<",(0,1):">"}

@functools.cache
def getCoordinates(array, value):
    return [(y, _.index(value)) for y, _ in enumerate(array) if value in _][0]

def getSequence(array,start,end):
    diff = (end[0] - start[0],end[1] - start[1])
    sequence = []

    def getY(diff,sequence):
        if(diff[0] < 0):
            #sequence.extend([(-1,0)] * abs(diff[0]))
            sequence.extend([directions[(-1,0)]] * abs(diff[0]))
        elif(diff[0] > 0):
            #sequence.extend([(1,0)] * abs(diff[0]))
            sequence.extend([directions[(1,0)]] * abs(diff[0]))
            
    def getX(diff,sequence):
        if(diff[1] < 0):
            #sequence.extend([(0,-1)] * abs(diff[1]))
            sequence.extend([directions[(0,-1)]] * abs(diff[1]))
        elif(diff[1] > 0):
            #sequence.extend([(0,1)] * abs(diff[1]))
            sequence.extend([directions[(0,1)]] * abs(diff[1]))
            
    #if("." in list(zip(*array))[end[1]]):
    if("." in array[end[0]]):
        getY(diff,sequence)
        getX(diff,sequence)
    else:
        getX(diff,sequence)
        getY(diff,sequence)
        
    sequence.append("A")
    return sequence

sequences = []

for cmd in cmds:
    numPart = int("".join(cmd[:-1]))

    start = getCoordinates(numericKeypad,"A")
    sequence = []
    while cmd:
        end = getCoordinates(numericKeypad,cmd.pop(0))
        sequence.extend(tuple(getSequence(numericKeypad,start,end)))
        start = end
    print("".join(sequence))
    for x in range(2):
        start = getCoordinates(directionalKeypad,"A")
        sequence2 = []
        while sequence:
            end = getCoordinates(directionalKeypad,sequence.pop(0))
            sequence2.extend(tuple(getSequence(directionalKeypad,start,end)))
            start = end
        sequence = sequence2
        print("".join(sequence))
    sequences.append(len(sequence) * numPart)

print(f"Part1: {sum(sequences)}")


# Zeit Ende
endeZeit = time.time()
print('Zeit:   {:.3f}s'.format(endeZeit-startZeit))


"""
029A: <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
      <vA<AA>>^AvAA<^A>Av<<A>>^AvA^A<vA>^Av<<A>^A>AAvA^Av<<A>A>^AAAvA<^A>A
      
980A: <v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A
      v<<A>>^AAAvA^A<vA<AA>>^AvAA<^A>Av<<A>A>^AAAvA<^A>A<vA>^A<A>A
      
179A: <v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
      v<<A>>^A<vA<A>>^AAvAA<^A>Av<<A>>^AAvA^A<vA>^AA<A>Av<<A>A>^AAAvA<^A>A
456A: <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A
      v<<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>Av<<A>A>^AAvA<^A>A
      
379A: <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
      <A>Av<<
      ^A<


      v<<A>>^AvA^Av<<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^AA<A>Av<<A>A>^AAAvA<^A>A

      ^A^^<<A>>AvvvA
      <A>A<AAv<AA>>^AvAA^A<vAAA>^A
      v<<A>>^AvA^Av<<A>>^A A<vA<A>>^AAvAA<^A>A<vA>^AA<A>Av<<A>A>^AAAvA<^A>A


<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
v<<A>>^A<A>AvA<^AA>A<vAAA>^A
<A^A>^^AvvvA
029A


+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
    
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""
