#!/usr/bin/env python3
import statistics as s
f = [int(_) for _ in [x.strip() for x in open("7.txt").readlines()][0].split(",")]
print(sum([abs(_-s.median(f)) for _ in f]))