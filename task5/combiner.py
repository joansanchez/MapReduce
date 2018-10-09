#!/usr/bin/env python2
import sys

range = []

for year in sys.stdin:
    if year != "\N":
        range.append(year.strip())
print ("task5" + "\t" + max(range) + "\t" + min(range))
