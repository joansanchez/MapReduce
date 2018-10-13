#!/usr/bin/env python2
#mapper.py
import sys

def map_function(line):
    new_line = line.split()
    i = 0
    while i < (len(new_line)-1):
        yield new_line[i]+"_"+new_line[i+1], 1
        i = i + 1



#main function
for line in sys.stdin:
    for key, value in map_function(line):
        print(key + "\t" + str(value))
