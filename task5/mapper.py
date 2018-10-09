#!/usr/bin/env python2
#mapper.py
import sys

#main function
for line in sys.stdin:
    new_line = line.strip().split("\t")
    for year in new_line[5].split(","):
        if year != "\N":
            print(year)
