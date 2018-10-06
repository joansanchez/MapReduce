#!/usr/bin/env python2
# mapper.py
import sys
import random

def map_function(document):
    # Split doucment by words and use word as the key
    rand_value = (random.randint(1,sys.maxint))%9
    yield str(rand_value), len(document.strip().split())


for line in sys.stdin:
    # Call map_function for each line in the input
    for key, value in map_function(line):
        # Emit key-value pairs using '\t' as a delimeter
        print(key + "\t" + str(value))
