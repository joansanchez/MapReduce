#!/usr/bin/env python2
#reducer.py
import sys

SUM_WRITERS = 0
NUM_TITLES = 0

for line in sys.stdin:
    titles, writers = line.strip().split("\t")
    SUM_WRITERS += int(writers)
    NUM_TITLES += int(titles)
result = SUM_WRITERS/float(NUM_TITLES)
result = int(round(result))
print(str(result))
