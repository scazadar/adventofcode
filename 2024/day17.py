#!/usr/bin/env python3
# Imports
import time,re

# Zeit Start
startZeit = time.time()

file = "2024/inputs/day17.sample"

i = open(file).read().split("\n\n")

register = [int(re.findall(r'[-\d]+', _)[0]) for _ in i[0].split("\n")]
programm = [int(re.findall(r'[-\d]+', _)[0]) for _ in i[1].split(",")]

print("".join([format(_,'03b') for _ in programm]))

opcodes = [_ for i,_ in enumerate(programm) if i % 2 == 0]
operands = [_ for i,_ in enumerate(programm) if i % 2 == 1]
cmds = list(zip(*[opcodes,operands]))

programmS = [str(_) for _ in programm]

def getComboOperand(operand):
    if(operand == 0):
        return operand
    elif(operand == 1):
        return operand
    elif(operand == 2):
        return operand
    elif(operand == 3):
        return operand
    elif(operand == 4):
        return register[0]
    elif(operand == 5):
        return register[1]
    elif(operand == 6):
        return register[2]
    elif(operand == 7):
        return None

def getOutput(register):
    pointer = 0
    output = []
    #print("============")
    #print(f"Start: {register}")
    while pointer < len(cmds):
        if(cmds[pointer][0] == 0):
            register[0] = register[0] // (2 ** getComboOperand(cmds[pointer][1]))
            #print(register)
            pointer += 1
        elif(cmds[pointer][0] == 1):
            register[1] = register[1] ^ cmds[pointer][1]
            pointer += 1
        elif(cmds[pointer][0] == 2):
            register[1] = (getComboOperand(cmds[pointer][1]) % 8) & 0b111
            pointer += 1
        elif(cmds[pointer][0] == 3):
            if(register[0] == 0):
                pointer += 1
            else:
                pointer = cmds[pointer][1] // 2
        elif(cmds[pointer][0] == 4):
            register[1] = register[1] ^ register[2]
            pointer += 1
        elif(cmds[pointer][0] == 5):
            output.append(str(getComboOperand(cmds[pointer][1]) % 8))
            if(programmS[:len(output)] != output):
                break
            pointer += 1
        elif(cmds[pointer][0] == 6):
            register[1] = register[0] // (2 ** getComboOperand(cmds[pointer][1]))
            pointer += 1
        elif(cmds[pointer][0] == 7):
            register[2] = register[0] // (2 ** getComboOperand(cmds[pointer][1]))
            pointer += 1

    return output

print(f"Part1: {",".join(getOutput(register))}")

print(programmS)
x = 134217727000000
n = 10000000000000

out = []
#programmS = ['3', '0']
while programmS != out:
    n += 1
    register = [n,0,0]
    out= getOutput(register)
    #print(out)
    #print("".join([format(int(_),'03b') for _ in out]))

#Program: 2,4,1,7,7,5,0,3,4,0,1,7,5,5,3,0
print(n)

# Zeit Ende
endeZeit = time.time()
print('Zeit:   {:.3f}s'.format(endeZeit-startZeit))
