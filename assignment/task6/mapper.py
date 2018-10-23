#!/usr/bin/env python2
#mapper.py
import sys

MAX_SIZE = 100
SUM_RATINGS = 0
NUM_RATINGS = 0

for line in sys.stdin:
    new_line = line.strip().split("\t")
    SUM_RATINGS = SUM_RATINGS + int(new_line[2])
    NUM_RATINGS += 1
    if NUM_RATINGS >= MAX_SIZE:
        print(str(SUM_RATINGS) + "\t" + str(NUM_RATINGS))
        NUM_RATINGS = 0
if NUM_RATINGS < MAX_SIZE:
    print(str(SUM_RATINGS) + "\t" + str(NUM_RATINGS))
