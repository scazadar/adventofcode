#!/usr/bin/env python3
from math import prod
line = [x.strip() for x in open("16.txt").readlines()][0]
CODE = bin(int(f'0x{line}',16))[2:].zfill(len(line)*4)

#print(CODE)
def parse(cursor):
    if(len(CODE[cursor:]) < 11):
        return cursor,[-1]
    VERSION = int(CODE[cursor:cursor+3],2)
    TYPE = int(CODE[cursor+3:cursor+6],2)
    cursor += 6
    versionsum = VERSION
    if(TYPE == 4):
        values = []
        group = []
        for x in range(int(len(CODE[cursor:])/5)):   
            seq = CODE[cursor:cursor+5]
            group.append(seq[1:])
            cursor += 5
            if(seq[0] == '0'):
                values = [(int("".join([_ for _ in group]),2))]
                break
        return cursor,values,versionsum
    else:
        TYPEID = int(CODE[cursor])
        cursor += 1
        values = []
        if(TYPEID == 0):
            TYPE_LENGTH = 15
            TOTAL_SUBPACKET_LENGTH = int(CODE[cursor:cursor+TYPE_LENGTH],2)
            cursor += TYPE_LENGTH
            paket_end = cursor + TOTAL_SUBPACKET_LENGTH
            while(cursor < paket_end):
                cursor,v,version = parse(cursor)
                versionsum += version
                if(v[0] >= 0):
                    values = values + v
        else:
            TYPE_LENGTH = 11
            NUMBER_OF_SUBPACKETS = int(CODE[cursor:cursor+TYPE_LENGTH],2)
            cursor += TYPE_LENGTH
            for _ in range(NUMBER_OF_SUBPACKETS):
                cursor,v,version = parse(cursor)
                versionsum += version
                if(v[0] >= 0):
                    values = values + v
        if(TYPE == 0):
            values = sum(values)
        elif(TYPE == 1):
            values = prod(values)
        elif(TYPE == 2):
            values = min(values)
        elif(TYPE == 3):
            values = max(values)
        elif(TYPE == 5):
            values = 1 if values[0] > values[1] else 0
        elif(TYPE == 6):
            values = 1 if values[0] < values[1] else 0
        elif(TYPE == 7):
            values = 1 if values[0] == values[1] else 0
        return cursor,[values],versionsum
    
c,value,versionsum = parse(0)
print(f"Value: {value[0]} Version: {versionsum}")