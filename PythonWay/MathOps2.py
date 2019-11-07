#!/bin/python3
# -*- coding: utf-8 -*-

import math
import os
import random
import re
import sys


def divInt(x, y): return x//y


def divFloat(x, y): return x/y


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(divInt(a, b))
    print(divFloat(a, b))
