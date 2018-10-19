#!/usr/bin/env python2
#reducer.py
import sys

decade = 0
prev_id = 0

for line in sys.stdin:
    line = line.strip().split(".")
    id = line[0]
    #print(line)
    #print(len(line[1]))
    if id != prev_id:
        if len(line[1]) == 4:
            #print ("change decade")
            decade = int(line[1])
        else:
            decade = 0
            #print ("no decade")
        prev_id = id
    if len(line[1]) != 4:
        if decade != 0:
            print (line[1])
