#!/bin/python3

import math
import os
import random
import re
import sys

def hourglass(s, f):
    count=0
    for i in range(s, s+3):
        for j in range(f, f+3):
            if i==s+1:
                if j==f+1:
                    count+=(arr[i][j])
            else:
                count+=arr[i][j]
    return count
    
if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    max_val=[]
    for i in range(4):
        for j in range(4):
            max_val.append(hourglass(i, j))
                        
    print(max(max_val))
