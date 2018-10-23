#!/usr/bin/env python2
#combiner.py
import sys

MAX_READ = 100
ACT_READ = 0
max_year = 0
min_year = 0
first_read = 1

#main function
for line in sys.stdin:
    tmp_min_year, tmp_max_year = line.strip().split("\t")
    if first_read == 1:
        max_year = tmp_max_year
        min_year = tmp_min_year
        first_read = 0
    if tmp_max_year > max_year:
        max_year = tmp_max_year
    if tmp_min_year < min_year:
        min_year = tmp_min_year
    ACT_READ += 1
    if ACT_READ >= MAX_READ:
        print (str(min_year) + "\t" + str(max_year))
        ACT_READ = 0
if ACT_READ < MAX_READ:
    print (str(min_year) + "\t" + str(max_year))
