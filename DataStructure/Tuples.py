#!/home/maia/.pyenv/versions/3.7.4/bin/python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())
    integer_list = map(int, input().split())
    integer_tuple = tuple(integer_list)
    hash_value = hash(integer_tuple)
    print(hash_value)
