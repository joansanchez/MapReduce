#!/usr/bin/env python2
#reducer2.py
import sys

prev_decade = None
values = []
first = 1

def getFinalAverage():
    str1 = ''.join(values)
    newValues = str1.strip().split(",")
    averageDcd = sum(map(float,newValues))
    return averageDcd/len(newValues)

for line in sys.stdin:
    line = line.strip().split("\t")
    decade = line[0]
    if decade != prev_decade and prev_decade is not None:
        average = getFinalAverage()
        g = round(average,1)
        print (prev_decade + "\t" + str(g) + "\t")
        values = []
        first = 1
    prev_decade = decade
    if first == 0:
        values.append(",")
    else:
        first = 0
    values.append(line[1])
if prev_decade is not None:
    average = getFinalAverage()
    g = round(average,1)
    print (prev_decade + "\t" + str(g) + "\t")
