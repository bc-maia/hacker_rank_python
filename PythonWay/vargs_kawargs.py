#!/bin/python3
# -*- coding: utf-8 -*-
from pprint import pprint
from random import randrange


def test_args(param1, *args_params):
    print(f"param1 value: {param1}")

    if args_params:
        print(f"many_params value:")
        for i in args_params:
            pprint(i)


def test_kwargs(param1, **kwargs_params):
    print(f"param1 value: {param1}")

    if kwargs_params:
        print(f"many_params value:")
        for i in kwargs_params:
            pprint(f"{i} : {kwargs_params[i]}")


def main():
    test_args("*args - no extra params")
    sample_params = range(2, 66, 26)
    test_args("with params", list(sample_params))
    test_args("with params", *sample_params)  # unpacking operators

    test_kwargs("**kwargs - no extra params")
    test_kwargs("**kwargs - using extra params", key=12345, val="abcde")


if __name__ == "__main__":
    main()
