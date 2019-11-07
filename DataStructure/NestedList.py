"""
# Input Format
The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines; 
the first line contains a student's name,
and the second line contains their grade.

# Constraints
There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics;
if there are multiple students, order their names alphabetically and print each one on a new line.

SAMPLE INPUT:

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

SAMPLE OUTPUT:
Berry
Harry
"""

if __name__ == "__main__":
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    _, scores = zip(*students)
    second_score = sorted(set(scores))[1]  # Set removes duplicated scores

    names = [name for name, score in students if score == second_score]

    for name in sorted(names):
        print(name)
