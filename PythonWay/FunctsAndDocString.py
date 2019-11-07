#!/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime


def year_prep(year):
    if year < datetime.now().year:
        return f"Was {year}"
    elif year > datetime.now().year:
        return f"Will {year} be"
    else:
        return f"Is {year}"


def is_leap(year):
    """
    This  is a leap year calculator

        input the year
    """
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
    return leap


if __name__ == "__main__":
    print(is_leap.__doc__)

    year = int(input("Input year: "))
    print(f"{year_prep(year)} a leap year? {is_leap(year)}\n")

    for y in range(1980, 1985):
        print(f"{year_prep(y)} a leap year? {is_leap(y)}")
