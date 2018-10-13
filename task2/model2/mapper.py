#!/usr/bin/env python2
#mapper.py
import sys
import collections

MAX_SIZE = 100
dict = collections.OrderedDict()

def map_function(line):
    new_line = line.split()
    i = 0
    while i < (len(new_line)-1):
        yield new_line[i]+"_"+new_line[i+1], 1
        i = i + 1



#main function
for line in sys.stdin:
    for key, value in map_function(line):
        if key in dict:
            dict[key] = dict[key] + value
        else:
            dict[key] = value
        if len(dict) >= MAX_SIZE:
            for word, word_count in dict.items():
                print(word + "\t" + str(word_count))
            dict.clear()
if len(dict) < MAX_SIZE:
    for word, word_count in dict.items():
        print(word + "\t" + str(word_count))
