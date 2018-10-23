#!/usr/bin/env python2
#combiner.py
import sys

MAX_SIZE = 100
NUM_WRITERS = 0
NUM_TITLES = 0
NUM_READS = 0

for line in sys.stdin:
    titles, writers = line.strip().split("\t")
    NUM_TITLES += int(titles)
    NUM_WRITERS += int(writers)
    NUM_READS += 1
    if NUM_READS >= MAX_SIZE:
        print (str(NUM_TITLES) + "\t" + str(NUM_WRITERS))
        NUM_TITLES = 0
        NUM_WRITERS = 0
        NUM_READS = 0
if NUM_READS < MAX_SIZE:
    print (str(NUM_TITLES) + "\t" + str(NUM_WRITERS))
