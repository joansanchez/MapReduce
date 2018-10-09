#!/usr/bin/env python2
import sys

prev_key = None

for line in sys.stdin:
    # Parse key and value
    key = line.strip().split('\t')

     # If key has changed then one can finish processing the previoos key
    if key != prev_key and prev_key is not None:
        print(key +  "\t")

    prev_key = key

# Don't forget about the last value!
if prev_key is not None:
    print(prev_key +  "\t")
