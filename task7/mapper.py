#!/usr/bin/env python2
#mapper.py
import sys

MAX_SIZE = 100
NUM_WRITERS = 0
NUM_TITLES = 0

for line in sys.stdin:
    new_line = line.strip().split("\t")
    if new_line[2] != "\N":
        writers = new_line[2].strip().split(",")
        NUM_WRITERS += len(writers)
        NUM_TITLES += 1
    if NUM_TITLES >= MAX_SIZE:
        print (str(NUM_TITLES) + "\t" + str(NUM_WRITERS))
        NUM_TITLES = 0
        NUM_WRITERS = 0
if NUM_TITLES < MAX_SIZE:
    print (str(NUM_TITLES) + "\t" + str(NUM_WRITERS))
