import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    result = [0, 0]
    for val_a, val_b in zip(a, b):
        if val_a > val_b:
            result[0] += 1
        if val_a < val_b:
            result[1] += 1
    return result


if __name__ == "__main__":
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(" ".join(map(str, result)))
