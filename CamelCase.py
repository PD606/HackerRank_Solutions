#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    i=0
    c=0
    while(i<len(s)):
        if(s[i].isupper()):
            c+=1
            i+=1
        else:
            i+=1
    return(c+1)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
