#!/usr/bin/env python2
#mapper.py
import sys

generes = {}
MAX_VALUES = 100
ACT_VALUES = 0

for line in sys.stdin:
    line = line.strip().split("\t")
    genere = line[8]
    startYear = line[5]
    if genere != "\N" and startYear != "\N":
        if int(startYear) >= 2000 and int(startYear) <= 2014:
            for difGen in genere.split(","):
                if difGen not in generes:
                    generes[difGen] = 1
                else:
                    generes[difGen] += 1
                ACT_VALUES += 1
                if ACT_VALUES >= MAX_VALUES:
                    for values in generes:
                        print(values + "\t" + str(generes[values]))
                    generes.clear()
                    ACT_VALUES = 0
if ACT_VALUES < MAX_VALUES:
    for values in generes:
        print(values + "\t" + str(generes[values]))
