#!/usr/bin/env python2
#mapper1.py
import sys

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) == 9: #reducer OUTPUT_FILE
        if parts[5] != "\N":
            year = int(parts[5])
            if year >= 1900 and year <= 1999:
                print (parts[0] + "\t" + "year" + "\t" + parts[5] + "\t")
    else:   #avarage file
        print (parts[0] + "\t" + "average" + "\t" + parts[1] + "\t")
