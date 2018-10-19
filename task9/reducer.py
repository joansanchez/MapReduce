#!/usr/bin/env python2
# reducer.py
import sys


prev_deca = None
values = 0

for line in sys.stdin:
    # Parse deca and value
    deca, value = line.strip().split('\t')

     # If deca has changed then one can finish processing the previoos deca
    if deca != prev_deca and prev_deca is not None:
        print(prev_deca + "\t" + str(values))
        values = 0

    prev_deca = deca
    values += int(value)


# Don't forget about the last value!
if prev_deca is not None:
    print(prev_deca + "\t" + str(values))
