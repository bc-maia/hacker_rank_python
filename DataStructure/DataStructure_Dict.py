#!/home/maia/.pyenv/versions/3.7.4/bin/python3
# -*- coding: utf-8 -*-


def find_average(arr):
    result = sum(arr) / len(arr)
    print(format(result, ".2f"))


if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks.keys():
        find_average(student_marks[query_name])
