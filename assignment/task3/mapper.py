#!/usr/bin/env python2
#mapper.py
import sys

Number_actors = 0
Max_actors = 100

#main function
for line in sys.stdin:
    new_line = line.strip().split("\t")
    for profession in new_line[4].split(","):
        if profession != "\N" and profession == "actor" or profession == "actress":
            Number_actors = Number_actors + 1
            if Number_actors >= Max_actors:
                print (str(Number_actors))
                Number_actors = 0
if Number_actors < Max_actors:
    print (str(Number_actors))
