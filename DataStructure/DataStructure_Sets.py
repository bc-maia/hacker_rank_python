#!/home/maia/.pyenv/versions/3.7.4/bin/python3
# -*- coding: utf-8 -*-


def find_runner_up(arr):
    score = sorted(arr)[-2]
    return score


if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())  # transforming input list into integers
    arr = set(arr)  # removing duplicates
    score = find_runner_up(list(arr))
    print(score)
