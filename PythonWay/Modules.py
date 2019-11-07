#!/bin/python3
# -*- coding: utf-8 -*-
import sys
from pprint import pprint
import sample_mod


def main():
    pprint(sys.path)
    """using modules pprint and sys
    to output prettier python system variables"""


if __name__ == "__main__":
    main()
    print(f"sample module imported version: {sample_mod.__version__}")

__version__ = "0.1"
