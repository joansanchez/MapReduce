#!/usr/bin/env python2
# reducer.py
import sys

lines = 0
words = 0

for line in sys.stdin:
    key, value = line.strip().split('\t')
    lines = lines + int(value)
    words = words + int(key)

print(str(words) + "\t" + str(lines))
