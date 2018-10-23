#!/usr/bin/env python2
#reducer.py
import sys

Number_actors = 0


for line in sys.stdin:
    Number_actors = Number_actors + int(line)
print (str(Number_actors))
