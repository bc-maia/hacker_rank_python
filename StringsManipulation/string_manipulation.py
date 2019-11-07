from os import system as ss

ss("clear")


def create_mat(height, width) -> list:
    mat = [None for _ in range(height)]

    template = ".|."

    triangles = [i for i in range(1, height) if i % 2 != 0]

    middle_line = "WELCOME".center(width, "-")
    half = int((height - 1) / 2)
    mat[half] = middle_line

    lower_line = [-i for i in range(1, half + 1) if i <= half]

    for upper, lower, tris in zip(range(height), lower_line, triangles):
        mat[upper] = mat[lower] = (tris * template).center(width, "-")
        if upper == half:
            break

    return mat


N, M = map(int, input().split(" "))
for line in create_mat(N, M):
    print(line)

"""
MAT is N x M of size, being M = 3 * N
'WELCOME' in the center
Pattern using: . | -

5 < N < 101
15 < M < 303

input: 7 x 21 
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
    
input: 11 x 33
---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------

input: 9 x 27
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

alt solution

n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
"""
