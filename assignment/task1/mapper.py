#!/usr/bin/env python2
# mapper.py
import sys

lines = 0
words = 0
MAX_SIZE = 100
LINES_READ = 0

for line in sys.stdin:
    lines = lines + 1
    words = words + len(line.strip().split())
    LINES_READ = LINES_READ + 1

    # To keep O(1) space, we bound the size of our memory footprint
    if LINES_READ >= MAX_SIZE:
        print(str(words) + "\t" + str(lines))
        LINES_READ = 0
        lines = 0
        words = 0

if LINES_READ != 0:
    print(str(words) + "\t" + str(lines))
