#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

arr=[]
# print(a)
for i in range(0,d):
    arr.append(a[i])

# print(arr)
a=a+arr
# print(a)

for i in range(d,len(a)):
    print(a[i],'' ,end='')
# for i in range (d,len(a)-1):
#     print(a)








