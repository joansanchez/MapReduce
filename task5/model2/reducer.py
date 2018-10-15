#!/usr/bin/env python2
#reducer.py
import sys

max_year = 0
min_year = 0
first_read = 1

for line in sys.stdin:
    tmp_min, tmp_max = line.strip().split("\t")
    if first_read == 1:
        max_year = tmp_max
        min_year = tmp_min
        first_read = 0
    if tmp_max > max_year:
        max_year = tmp_max
    if tmp_min < min_year:
        min_year = tmp_min
print (str(min_year)+"\t"+str(max_year))
