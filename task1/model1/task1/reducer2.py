#!/usr/bin/env python2
import sys

def reduce_function(sumWords):
    # Calculate how many times each word was encountered
    return len(sumWords), sum(sumWords)

values = []

for line in sys.stdin:
    # Parse key and value
    key, value = line.strip().split('\t')
    values.append(int(value))
    
result_key, result_value = reduce_function(values)
print(str(result_value) + "\t" + str(result_key))
