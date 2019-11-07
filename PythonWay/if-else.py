#!/bin/python3
# -*- coding: utf-8 -*-

import math
import os
import random
import re
import sys


def check_even_odd(user_input):
    if user_input % 2 != 0:
        print("Weird")
    elif user_input in range(2, 6):
        print("Not Weird")
    elif user_input in range(6, 21):
        print("Weird")
    elif user_input > 20:
        print("Not Weird")


def main():
    n = int(input().strip())
    if n >= 1 and n <= 100:
        check_even_odd(n)
    else:
        pass


if __name__ == "__main__":
    main()
