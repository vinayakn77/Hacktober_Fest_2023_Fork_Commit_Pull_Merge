# Hackerrank

# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    start_max = scores[0]
    start_min = scores[0]
    max_rec = 0
    min_rec = 0
    result = []
    
    for i in scores:
        if i > start_max:
            start_max = i
            max_rec += 1
            
    for i in scores:
        if i < start_min:
            start_min = i
            min_rec += 1
            
    result.append(max_rec)
    result.append(min_rec)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()