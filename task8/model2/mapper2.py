#!/usr/bin/env python2
#mapper2.py
import sys

decades = {}
MAX_VALUES = 100
ACT_VALUE = 0

def avgDecade(decade):
    averageDcd = sum(map(float,decades[decade]))
    return averageDcd/len(decades[decade])

for line in sys.stdin:
    line = line.strip().split("\t")
    year = line[0]
    if year not in decades:
        decades[year] = []
    decades[year].append(float(line[1]))
    ACT_VALUE += 1
    if ACT_VALUE >= MAX_VALUES:
        for values in decades:
            average_decade = avgDecade(values)
            print (values + "\t" + str(average_decade) + "\t" + str(len(decades[values])))
        ACT_VALUE = 0
        decades.clear()
if ACT_VALUE < MAX_VALUES:
    for values in decades:
        average_decade = avgDecade(values)
        print (values + "\t" + str(average_decade) + "\t" + str(len(decades[values])))
