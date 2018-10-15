#!/usr/bin/env python2
#combiner.py
import sys

MAX_SIZE = 100
SUM_RATINGS = 0
NUM_RATINGS = 0

for line in sys.stdin:
    VOTES, NUM_VOTES = line.strip().split("\t")
    SUM_RATINGS = SUM_RATINGS + int(VOTES)
    NUM_RATINGS += int(NUM_VOTES)
    if NUM_RATINGS >= MAX_SIZE:
        print(str(SUM_RATINGS) + "\t" + str(NUM_RATINGS))
        NUM_RATINGS = 0
if NUM_RATINGS < MAX_SIZE:
    print(str(SUM_RATINGS) + "\t" + str(NUM_RATINGS))
