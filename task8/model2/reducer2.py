#!/usr/bin/env python2
#reducer2.py
import sys

prev_decade = None
values = []
numFilms = 0

def getFinalAverage():
    averageDcd = sum(map(float,values))
    return averageDcd/numFilms

for line in sys.stdin:
    line = line.strip().split("\t")
    decade = line[0]
    avg = float(line[1])
    if decade != prev_decade and prev_decade is not None:
        average = getFinalAverage()
        g = round(average,1)
        print (prev_decade + "\t" + str(g) + "\t")
        values = []
        numFilms = 0
    prev_decade = decade
    values.append(avg)
    numFilms += int(line[2])
if prev_decade is not None:
    average = getFinalAverage()
    g = round(average,1)
    print (prev_decade + "\t" + str(g) + "\t")
