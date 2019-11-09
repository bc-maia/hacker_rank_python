from itertools import product

if __name__ == "__main__":
    a = input().split(" ")
    b = input().split(" ")
    a = map(int, a)
    b = map(int, b)
    print(*product(a, b))

    # alt way:
    # prodct = ((int(x), int(y)) for x in a for y in b)
    # print(*prodct)
