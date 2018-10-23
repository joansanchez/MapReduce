#!/usr/bin/env python2
#mapper.py
import sys

generes = set()
MAX_SIZE = 100


for line in sys.stdin:
    new_line = line.strip().split("\t")
    for genere in new_line[8].split(","):
        if genere != "\N":
            if genere not in generes:
                generes.add(genere)
            if len(generes)>= MAX_SIZE:
                for word in generes:
                    print(word)
                generes.clear()
if len(generes) < MAX_SIZE:
    for word in generes:
        print(word)
