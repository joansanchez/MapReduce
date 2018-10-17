#!/usr/bin/env python2
#combiner2.py
import sys

LINES_READ = 0
MAX_LINES = 100
decade_ratings = {}

def printFilms():
    for decade in decade_ratings:
        avarage = 0.0
        for avaragetmp in decade_ratings[decade]:
            avarage += avaragetmp
        print(decade + "\t" + str(avarage/len(decade_ratings[decade])) + "\t" + str(len(decade_ratings[decade])))
    decade_ratings.clear()
    LINES_READ = 0

for line in sys.stdin:
    rating = line.strip().split("\t")
    if rating[0] not in decade_ratings:
        decade_ratings[rating[0]] = []
    decade_ratings[rating[0]].append(float(rating[1]))
    LINES_READ += 1
    if LINES_READ >= MAX_LINES:
        printFilms()
if LINES_READ < MAX_LINES:
    printFilms()
