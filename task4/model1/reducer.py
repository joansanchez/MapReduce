#!/usr/bin/env python2
import sys

prev_key = None

for key in sys.stdin:

     # If key has changed then one can finish processing the previoos key
    if key != prev_key and prev_key is not None:
        print(prev_key.strip())

    prev_key = key

# Don't forget about the last value!
if prev_key is not None:
    print(prev_key.strip())
