
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    reversed_arr = []

    for i in range(n):
        reversed_arr.append(arr[n-i-1])

    print(' '.join(str(i)for i in reversed_arr))

