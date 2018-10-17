#!/usr/bin/env python2
#mapper2.py
import sys

set_ids = {}
NUM_FILMS = 0
decade = 0
AVARAGE = 0.0

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) == 2: #reducer OUTPUT_FILE
        decade = parts[0]
        set_ids = set(parts[1].strip().split(","))
    else:   #avarage file
        if parts[0] in set_ids:
            AVARAGE += float(parts[1])
            NUM_FILMS += 1
if NUM_FILMS > 0:
    print (str(decade) + "\t" + str(AVARAGE/NUM_FILMS))
