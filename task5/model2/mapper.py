#!/usr/bin/env python2
#mapper.py
import sys

MAX_READ = 100
ACT_READ = 0
max_year = 0
min_year = 0
first_read = 1

#main function
for line in sys.stdin:
    new_line = line.strip().split("\t")
    year = new_line[5]
    if year != "\N":
        if first_read == 1:
            max_year = year
            min_year = year
            first_read = 0
        if year > max_year:
            max_year = year
        if year < min_year:
            min_year = year
        ACT_READ += 1
        if ACT_READ >= MAX_READ:
            print (str(min_year) + "\t" + str(max_year))
            ACT_READ = 0
if ACT_READ < MAX_READ:
    print (str(min_year) + "\t" + str(max_year))
