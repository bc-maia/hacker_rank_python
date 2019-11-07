#!/bin/python3
# -*- coding: utf-8 -*-

import math
import os
import random
import re
import sys


def su(x, y):
    return x + y


def subt(x, y):
    return x - y


def prod(x, y):
    return x * y


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(su(a, b))
    print(subt(a, b))
    print(prod(a, b))
