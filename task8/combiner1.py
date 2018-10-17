#!/usr/bin/env python2
#combiner1.py
import sys

MAX_VALUES = 100
ITEMS_READ = 0
dict = {}

for line in sys.stdin:
    decade, ids = line.strip().split("\t")
    decade = int(decade)
    if decade not in dict:
        dict[decade] = []
    dict[decade].append(ids)
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
