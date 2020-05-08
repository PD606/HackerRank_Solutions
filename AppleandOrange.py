#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.


def countApplesAndOranges(s, t, a, b, apples, oranges):
    ap=0
    org=0

    for i in range(0,len(apples)):
        p=a+apples[i]
        # print(p)
        if(p>=s and p <=t):
            ap+=1
        else:
            pass
    print(ap)

    for k in range(0,len(oranges)):
        q=b+oranges[k]
        if(q>=s and q <=t):
            org+=1
        else:
            pass
    print(org)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
