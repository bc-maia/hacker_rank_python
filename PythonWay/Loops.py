#!/bin/python3
# -*- coding: utf-8 -*-

import math
import os
import random
import re
import sys


def loop_pow(limit, n=0):
    if n < limit:
        print(n ** 2)
        loop_pow(limit, n + 1)


if __name__ == "__main__":
    limit = int(input())
    loop_pow(limit)
