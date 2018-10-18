#!/usr/bin/env python2
#mapper2.py
import sys
import random

set_ids = {} #dict with id_film:decade
ratings = {} #dict with id_fils:rating


for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) == 2: #reducer OUTPUT_FILE
        ids = parts[1].split(',')
        for film in ids:
            set_ids[film] = parts[0]
    else:   #avarage file
        ratings[parts[0]] = parts[1]
g = random.randint(1,100000000001)
print (str(g) + str(set_ids))
print (str(g) + str(ratings))
