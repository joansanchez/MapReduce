#!/usr/bin/env python2
# combiner.py
import sys

lines = 0
words = 0
MAX_SIZE = 100
LINES_READ = 0

for line in sys.stdin:
    key, value = line.strip().split('\t')
    lines = lines + int(value)
    words = words + int(key)
    LINES_READ = LINES_READ + 1

    # To keep O(1) space, we bound the size of our memory footprint
    if LINES_READ >= MAX_SIZE:
        print(str(words) + "\t" + str(lines))
        LINES_READ = 0
        lines = 0
        words = 0

if LINES_READ != 0:
    print(str(words) + "\t" + str(lines))
