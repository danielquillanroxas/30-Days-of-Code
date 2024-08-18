#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    total = 0
    totals = []
    binn = bin(n).replace("0b", "")
    # print(binn)
    for i in range(len(binn)):
        if binn[i] == '1':
            total += 1
            totals.append(total)
        else:
            total = 0
            totals.append(total)
    print(max(totals))
