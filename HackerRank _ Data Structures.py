#!/usr/bin/env python
# coding: utf-8

# # Arrays - DS 
# https://www.hackerrank.com/challenges/arrays-ds/problem

# ### Final Code

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
# There's a general rule that states - in a matrix, the total number of hourglass is (R-2) * (C-2)
def hg_sum(arr_, i, j):
    hg_sum_ = arr_[i][j] + arr_[i][j+1] + arr_[i][j+2] + arr_[i+1][j+1] + arr_[i+2][j] + arr_[i+2][j+1] + arr_[i+2][j+2]
    return hg_sum_

def hourglassSum(arr):
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            total_ = hg_sum(arr, i, j)
            global max_sum
            max_sum = max(total_, max_sum)
    print(max_sum)
    return max_sum

if __name__ == '__main__':
    arr = []
    total_ = 0
    max_sum = -1073741824
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

