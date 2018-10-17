#!/usr/bin/env python2
#mapper1.py
import sys

MAX_VALUES = 100
ITEMS_READ = 0
dict = {}

for line in sys.stdin:
    new_line = line.strip().split("\t")
    if new_line[5] != "\N":
        year = int(new_line[5])
        if year >= 1900 and year <= 1999:
            year = year - year%10   #gives us the decade
            if year not in dict:
                dict[year] = []
            dict[year].append(new_line[0])
            ITEMS_READ += 1
            if ITEMS_READ >= MAX_VALUES:
                for items in dict.items():
                    separator = ","
                    print (str(items) + "\t" + separator.join(dict[items]))
                ITEMS_READ = 0
                dict.clear()
if ITEMS_READ < MAX_VALUES:
    for key, ids in dict.items():
        separator = ","
        print (str(key) + "\t" + separator.join(ids))
