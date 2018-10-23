#!/usr/bin/env python2
#reducer.py
import sys

SUM_RATINGS = 0
NUM_RATINGS = 0

for line in sys.stdin:
    VOTES, NUM_VOTES = line.strip().split("\t")
    SUM_RATINGS = SUM_RATINGS + int(VOTES)
    NUM_RATINGS += int(NUM_VOTES)
result = SUM_RATINGS/float(NUM_RATINGS)
g = float("{0:.2f}".format(result))
print(str(g))
