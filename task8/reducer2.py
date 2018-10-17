#!/usr/bin/env python2
#reducer2.py
import sys
from decimal import Decimal


prev_decade = None
average = 0.0
nfilms = 0


for line in sys.stdin:
    decade, averagetmp, nfilmstmp = line.strip().split("\t")

    if decade != prev_decade and prev_decade is not None:
        g = average/nfilms
        g = round(g,1)
        print(prev_decade + "\t" + str(g) + "\t")
        average = 0.0
        nfilms = 0

    prev_decade = decade
    average += float(averagetmp)
    nfilms += 1

# Don't forget about the last value!
if prev_decade is not None:
    g = average/nfilms
    g = round(g,1)
    print(prev_decade + "\t" + str(g) + "\t")
