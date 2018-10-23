#!/usr/bin/env python2
#combiner.py
#not in use in this case
import sys

generes = set()
MAX_SIZE = 100


for genere in sys.stdin:
    if genere not in generes:
        generes.add(genere.strip())
    if len(generes)>= MAX_SIZE:
        for word in generes:
            print(word)
        generes.clear()
if len(generes) < MAX_SIZE:
    for word in generes:
        print(word)
