#!/usr/bin/env python2
#combiner.py
import sys

Number_actors = 0
Max_actors = 100

for line in sys.stdin:
    Number_actors = Number_actors + int(line)
    if Number_actors >= Max_actors:
        print (str(Number_actors))
        Number_actors = 0
if Number_actors < Max_actors:
    print (str(Number_actors))
