#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.

l=[]
for i in range(97,123):
    l.append(chr(i))

# print(l)


def designerPdfViewer(h, word):
    # print(h)
    # print(word)
    m=[]
    d=dict(zip(l,h))
    # print(d)

    for i in word:
        m.append(d[i])

    return (max(m)*len(word))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
