#!/usr/bin/env python2
#combiner.py
import sys

prev_key = None
values = 0

for line in sys.stdin:
    # Parse key and value
    key, value = line.strip().split("\t")

     # If key has changed then one can finish processing the previoos key
    if key != prev_key and prev_key is not None:
        print(prev_key + "\t" + str(values))
        values = 0

    prev_key = key
    values += int(value)

# Don't forget about the last value!
if prev_key is not None:
    print(prev_key + "\t" + str(values))
