#!/usr/bin/env python2
import sys

new_dict = {}

for line in sys.stdin:
    # Parse key and value
    key, value = line.strip().split('\t')

    if key in new_dict:
        new_dict[key] = new_dict[key] + int(value)
    else:
        new_dict[key] = int(value)

for new_key, new_value in new_dict.items():
    print(new_key + "\t" + str(new_value))
