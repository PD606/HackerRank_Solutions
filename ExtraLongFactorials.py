#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    i=n
    s=1

    while(i>0):
        s*=(i)
        i-=1
    print(s)
if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
