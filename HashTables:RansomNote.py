#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    

    c=1
    d=dict()
    word=[]

    for i in magazine:
        word.append(i)
        if(i not in d):
            d[i]=1
        else:
            d[i]+=1

    # print(word)
    # print(d)

    for j in note:
        if(j not in word or d[j]==0):
            c=0
            break
        else:
            d[j]-=1
    
    if(c==1):
        print('Yes')
    else:
        print('No')
        

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
