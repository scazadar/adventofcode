#!/usr/bin/env python3
#Imports
import time, copy
from parse import parse
import numpy as np

#Zeit Start
start = time.time()

#Main
class monkey():
    def __init__(self,number,items,operation,test,nextmonkeys):
        self.number = number
        self.items = items
        self.new_items = []
        self.operation = operation
        self.test = test
        self.nextmonkeys = nextmonkeys
        self.inspected_items = 0

    def _inspect_item(self,old):
        if("old * old" in self.operation):
            new =old
        else:
            new = eval(self.operation.split("=")[1])
        self.inspected_items += 1
        return new

    def throw_items(self,divide):
        nextmonkeys = []
        for item in self.items:
            
            if(divide):
                item_worrylevel = self._inspect_item(item)//3
            else:
                item_worrylevel = self._inspect_item(item)
            #new_item_worrylevel = np.prod(list(set(self.PrimFaktorZerlegung(item_worrylevel))))

            if(item_worrylevel % self.test == 0):
            #if(self.test in self.PrimFaktorZerlegung(item_worrylevel)):
                nextmonkeys.append([self.nextmonkeys[0],item_worrylevel])
            else:
                nextmonkeys.append([self.nextmonkeys[1],item_worrylevel])
 
        self.items = []
        return nextmonkeys

    def PrimFaktorZerlegung(self,n):
        primzahlen = []
        i = 2
        while i <= n:
            while n % i == 0:
                primzahlen.append(i)
                n = n / i
            i = i + 1
        return primzahlen



input = [_.split("\n") for _ in open("inputs/day11.sample").read().split("\n\n")]
monkeys =  []
monkeys2 = []

#Affen erstellen
for monkey_input in input:
    number = parse("Monkey {:d}:", monkey_input[0])[0]
    items = list(map(int,parse("  Starting items: {}", monkey_input[1])[0].split(",")))
    operation = parse("  Operation: {}", monkey_input[2])[0]
    test = parse("  Test: divisible by {:d}", monkey_input[3])[0]
    nextmonkeys = [parse("    If true: throw to monkey {:d}", monkey_input[4])[0],parse("    If false: throw to monkey {:d}", monkey_input[5])[0]]
    
    monkeys.append(monkey(number,items,operation,test,nextmonkeys))

monkeys2 = copy.deepcopy(monkeys)

#Part 1
for round in range(20):
    for monkey in monkeys:
        for item in monkey.throw_items(True):
            monkeys[item[0]].items.append(item[1])

inspects = sorted([_.inspected_items for _ in monkeys])
print("Part 1: ", inspects[-1]*inspects[-2])
"""
#Part 2
for round in range(10000):
    for monkey in monkeys2:
        for item in monkey.throw_items(False):
            monkeys2[item[0]].items.append(item[1])

inspects = sorted([_.inspected_items for _ in monkeys2])
print("Part 2: ", inspects[-1]*inspects[-2])

"""





#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))
# 0.003s