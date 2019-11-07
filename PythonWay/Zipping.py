#!/home/maia/.pyenv/versions/3.7.4/bin/python3
# -*- coding: utf-8 -*-


def get_scores(n_students, x_subjects):
    scores = []
    for i in range(x_subjects):
        points = input().split(" ")
        float_scores = list(map(float, points))
        scores.append(float_scores)
    scores = zip(*scores)  # TODO: using * to unpack the list of lists
    return list(scores)


def get_average(group, x_subjects):
    average_scores = []
    for scores in group:
        avg = sum(scores) / x_subjects
        average_scores.append(avg)
    return average_scores


def print_scores(average_scores):
    # TODO: when need to format, remember to use format()
    for i in average_scores:
        print(format(i, ".2f"))


if __name__ == "__main__":
    user_input = input().strip().split(" ")
    n_students = int(user_input[0])
    x_subjects = int(user_input[-1])

    scores_list = get_scores(n_students, x_subjects)
    average_scores = get_average(scores_list, x_subjects)
    print_scores(average_scores)
