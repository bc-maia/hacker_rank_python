# -*- coding: utf-8 -*-
def find_average(arr):
    result = sum(arr) / len(arr)
    print(format(result, ".2f"))


if __name__ == "__main__":
    n = int(input())  # Number of students names + scores

    student_marks = {}
    for _ in range(n):
        name, *line = input().split()  # splits the students name + scores into an array
        scores = list(map(float, line))  # map applies the float into all values
        student_marks[name] = scores  # binds key, value dictionary

    query_name = input()

    if query_name in student_marks.keys():
        find_average(student_marks[query_name])
