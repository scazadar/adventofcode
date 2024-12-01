#!/usr/bin/env python3
#Imports
import time
from collections import deque

#Zeit Start
start = time.time()

#Main
f = [[int(_) for _ in _] for _ in open("2023/inputs/day17.sample").read().split("\n")]


queue = []
finished = []
nodes = {}





#Zeit Ende
ende = time.time()
print('Zeit:   {:.3f}s'.format(ende-start))