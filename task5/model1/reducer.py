#!/usr/bin/env python2
import sys

range = []

for range_years in sys.stdin:
    year = range_years.strip().split("\t")
    range.append(year[1])
    range.append(year[2])
print (min(range) + "\t" + max(range))
