#!/usr/bin/env python2
#reducer1.py
import sys

prev_id = None
year = 0
average = ""
complete = 0

for line in sys.stdin:
    id, action, value = line.strip().split("\t")
    if id != prev_id and prev_id is not None:
        if complete == 2:
            year = year - year%10
            print(str(year) + "\t" + average + "\t")
        year = ""
        average = ""
        complete = 0

    prev_id = id
    complete += 1
    if action == "year":
        year = int(value)
    else:
        average = value

# Don't forget about the last value!
if prev_id is not None and complete == 2:
    year = year - year%10
    print(str(year) + "\t" + average + "\t")
