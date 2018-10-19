#!/usr/bin/env python2
#mapper.py
import sys

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) == 6:
        for titles in parts[5].split(","):
            if titles != "\N":
                print(titles + "." + parts[0])

    else:
        if parts[5] != "\N":
            year = int(parts[5])
            if year >= 2010 and year <= 2018:
                print (parts[0] + "." + parts[5])
