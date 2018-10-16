#!/usr/bin/env python2
#combiner.py
import sys
import collections
#NOT IN USE - NOT WORKING PROPERLY
MAX_SIZE = 100
dict = collections.OrderedDict()

#main function
for line in sys.stdin:
    key, value = line.strip().split("\t")
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
