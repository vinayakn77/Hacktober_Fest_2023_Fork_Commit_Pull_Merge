# Hackerrank
# https://www.hackerrank.com/challenges/one-week-preparation-kit-caesar-cipher-1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    result = []
    for i in s:
        if i.isalpha():
            if i.isupper():
                next_alpha = (ord(i) + k - ord('A')) % 26 + ord('A')
            else:
                next_alpha = (ord(i) + k - ord('a')) % 26 + ord('a')
            result.append(chr(next_alpha))
        else:
            result.append(i)
            
    return ''.join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()