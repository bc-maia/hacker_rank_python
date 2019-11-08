from os import system as ss

ss("clear")


def get_char_list(length):
    letters = [chr(letter) for letter in range(ord("a"), ord("a") + length)]
    return list(reversed(letters))


def draw_rangoli(chars):
    # Size defined middle line lenth after "-" join and center
    length = (len(chars) * 4) - 3

    upper_lines = []
    for i, _ in enumerate(chars):
        chunk = chars[: i + 1]
        chunk = chunk + chunk[::-1][1:]
        line = "-".join(chunk).center(length, "-")
        upper_lines.append(line)
    lower_lines = upper_lines[:-1][::-1]

    return upper_lines + lower_lines

    # TODO: as list comprehension
    # upper_lines = [
    #     chars[: i + 1] + chars[: i + 1][::-1][1:] for i, char in enumerate(chars)
    # ]


def print_rangoli(size):
    characters = get_char_list(size)
    rangoli = draw_rangoli(characters)
    for line in rangoli:
        print(line)


if __name__ == "__main__":
    size = int(input())
    print_rangoli(size)


# TODO: Draw an Indian Rangoli
"""
Sample Input:
5

Sample Output:
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
