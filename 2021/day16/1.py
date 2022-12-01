#!/usr/bin/env python3
line = [x.strip() for x in open("16.txt").readlines()][0]
CODE = bin(int(f'0x{line}',16))[2:].zfill(len(line)*4)

def parse_literal(cursor):
    group = []
    for x in range(int(len(CODE[cursor:])/5)):   
        seq = CODE[cursor:cursor+5]
        group.append(seq[1:])
        cursor += 5
        if(seq[0] == '0'):
            break
    return cursor

def parse_object(cursor,versionsum):
    TYPEID = int(CODE[cursor])
    cursor += 1
    if(TYPEID == 0):
        TYPE_LENGTH = 15
        TOTAL_SUBPACKET_LENGTH = int(CODE[cursor:cursor+TYPE_LENGTH],2)
        cursor += TYPE_LENGTH
        paket_end = cursor + TOTAL_SUBPACKET_LENGTH
        while(cursor < paket_end):
            cursor,versionsum = parse(cursor,versionsum)
    else:
        TYPE_LENGTH = 11
        NUMBER_OF_SUBPACKETS = int(CODE[cursor:cursor+TYPE_LENGTH],2)
        cursor += TYPE_LENGTH
        for _ in range(NUMBER_OF_SUBPACKETS):
            cursor,versionsum = parse(cursor,versionsum)
    return cursor,versionsum


def parse(cursor,versionsum):
    if(len(CODE[cursor:]) < 11):
        return cursor,versionsum
    VERSION = int(CODE[cursor:cursor+3],2)
    versionsum += VERSION
    TYPE = int(CODE[cursor+3:cursor+6],2)
    cursor += 6
    if(TYPE == 4):
        cursor = parse_literal(cursor)
    else:
        cursor,versionsum = parse_object(cursor,versionsum) 
    return cursor,versionsum

c,versionsum = parse(0,0)
      
print(f"Version: {versionsum}")