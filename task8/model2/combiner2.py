#!/usr/bin/env python2
#combiner2.py
import sys

decades = {}
MAX_VALUES = 100
ACT_VALUE = 0

for line in sys.stdin:
    line = line.strip().split("\t")
    year = line[0]
    if year not in decades:
        decades[year] = float(line[1])
    else:
        decades[year] = (decades[year] + float(line[1]))/2
    ACT_VALUE += 1
    if ACT_VALUE >= MAX_VALUES:
        for values in decades:
            print (values + "\t" + str(decades[values]))
        ACT_VALUE = 0
        decades.clear()
if ACT_VALUE < MAX_VALUES:
    for values in decades:
        print (values + "\t" + str(decades[values]))
