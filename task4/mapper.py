#!/usr/bin/env python2
#mapper.py
import sys


#main function
for line in sys.stdin:
    new_line = line.strip().split("\t")
    for genere in new_line[8].split(","):
        print(genere)
