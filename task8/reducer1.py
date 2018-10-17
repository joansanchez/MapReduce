#!/usr/bin/env python2
#reducer1.py
import sys

prev_key = None
values = []

for line in sys.stdin:
    key, value = line.strip().split("\t")

    if key != prev_key and prev_key is not None:
        separator = ","
        print(prev_key + "\t" + separator.join(values))
        values = []

    prev_key = key
    values.append(value)

# Don't forget about the last value!
if prev_key is not None:
    separator = ","
    print(prev_key + "\t" + separator.join(values))
